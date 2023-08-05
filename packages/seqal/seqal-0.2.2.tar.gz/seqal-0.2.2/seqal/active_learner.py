from collections import namedtuple
from typing import Callable, List, Tuple

from flair.data import Sentence
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer
from torch.nn import Module

from seqal.datasets import Corpus

LabelInfo = namedtuple("LabelInfo", "idx text label")


def predict_data_pool(sents: List[Sentence], tagger: Module) -> None:
    """Predict on data pool for query.

    Args:
        sents (List[Sentence]): Sentences in data pool.
        tagger (Module): Trained model.
    """
    for sent in sents:
        tagger.predict(sent)


def remove_query_samples(sents: List[Sentence], query_idx: List[int]) -> None:
    """Remove queried data from data pool.

    Args:
        sents (List[Sentence]): Sentences in data pool.
        query_idx (List[int]): Index list of queried data.
    """
    new_sents = []
    query_sents = []
    for i, sent in enumerate(sents):
        if i in query_idx:
            query_sents.append(sent)
        else:
            new_sents.append(sent)
    return new_sents, query_sents


def save_label_info(sents: List[Sentence]) -> List[List[LabelInfo]]:
    """Save label information before prediction in case of overwriting.

    Args:
        sents (List[Sentence]): Sentences in data pool.

    Returns:
        List[List[LabelInfo]]: Labels information in each sentence.
    """
    labels_info = []

    for sent in sents:
        sent_label_info = []
        if len(sent.get_spans("ner")) != 0:
            for token in sent:
                tag = token.get_tag("ner")
                sent_label_info.append(LabelInfo(token.idx, token.text, tag.value))
        labels_info.append(sent_label_info)

    return labels_info


def load_label_info(
    sents: List[Sentence], labels_info: List[List[LabelInfo]]
) -> List[Sentence]:
    """Load label infomation after prediction.

    Args:
        sents (List[Sentence]): Sentences in data pool.
        labels_info (List[List[LabelInfo]]): Labels information in each sentence.

    Returns:
        List[Sentence]: Sentences in data pool.
    """
    for idx_sent, sent_label_info in enumerate(labels_info):
        if len(sent_label_info) != 0:
            for idx_token, token_label_info in enumerate(sent_label_info):
                sents[idx_sent][idx_token].add_tag("ner", token_label_info.label)

    return sents


class ActiveLearner:
    """Active learning workflow class.

    Args:
        tagger: The tagger to be used in the active learning loop.
        query_strategy: Function providing the query strategy for the active learning loop,
            for instance, seqal.uncertainty.uncertainty_sampling.
        corpus: Corpus contains train(labeled data), dev, test (data pool).
        **trainer_params: keyword arguments.
    Attributes:
        tagger: The tagger to be used in the active learning loop.
        query_strategy: Function providing the query strategy for the active learning loop.
        corpus: The corpus to be used in active learning loop.
    """

    def __init__(
        self,
        tagger_params: dict,
        query_strategy: Callable,
        corpus: Corpus,
        trainer_params,
    ) -> None:
        assert callable(query_strategy), "query_strategy must be callable"
        self.tagger_params = tagger_params
        self.trained_tagger = None
        self.query_strategy = query_strategy
        self.corpus = corpus
        self.trainer_params = trainer_params

    def fit(self, save_path: str = "resources/init_train") -> None:
        """Train model on labeled data.

        Args:
            save_path (str, optional): Log and model save path. Defaults to "resources/init_train".
        """
        # Initialize sequence tagger
        tag_type = self.tagger_params["tag_type"]
        hidden_size = self.tagger_params["hidden_size"]
        embeddings = self.tagger_params["embeddings"]
        tag_dictionary = self.corpus.make_tag_dictionary(tag_type=tag_type)

        tagger = SequenceTagger(
            hidden_size=hidden_size,
            embeddings=embeddings,
            tag_dictionary=tag_dictionary,
            tag_type=tag_type,
        )

        trainer = ModelTrainer(tagger, self.corpus)
        trainer.train(save_path, **self.trainer_params)
        self.trained_tagger = tagger

    def query(
        self,
        sents: List[Sentence],
        query_number: int,
        token_based: bool = False,
        simulation_mode: bool = False,
    ) -> Tuple[List[Sentence], List[Sentence]]:
        """Query data from pool (sents).

        Args:
            sents (List[Sentence]): Data pool that consist of sentences.
            query_number (int): batch query number.
            token_based (bool, optional): If true, using query number as token number to query data.
                                          If false, using query number as sentence number to query data.
            simulation_mode (bool, optional): If ture, sents contains real NER tags.
                                              If false, sents do not contains NER tags.

        Returns:
            Tuple[List[Sentence], List[Sentence]]:
                sents: The data pool after removing query samples.
                query_samples: Query samples.
        """
        tag_type = self.tagger_params["tag_type"]

        if simulation_mode is True:
            # Save labels information before prediction in case of overwriting real NER tags.
            # This is because Flair will assign NER tags to token after prediction
            labels_info = save_label_info(sents)

        predict_data_pool(sents, self.trained_tagger)
        query_idx = self.query_strategy(sents, tag_type, query_number, token_based)

        if simulation_mode is True:
            # Reload the real NER labels
            sents = load_label_info(sents, labels_info)

        # Remove queried data from sents and create a new list to store queried data
        sents_after_remove, queried_samples = remove_query_samples(sents, query_idx)

        return sents_after_remove, queried_samples

    def teach(
        self, query_samples: Sentence, save_path: str = "resources/retrain"
    ) -> None:
        """Retrain model on new labeled dataset.

        Args:
            query_samples (Sentence): new labeled data.
            save_path (str, optional): Log and model save path. Defaults to "resources/retrain".
        """
        self.corpus.add_query_samples(query_samples)
        self.fit(save_path)
