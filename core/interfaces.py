from abc import ABC, abstractmethod


class BaseRetriever(ABC):
    """
    Minimal contract for retrieval implementations.

    Concrete retrievers can use any backing strategy, such as vector search,
    keyword search, or hybrid retrieval, as long as they return documents for a
    query.
    """

    @abstractmethod
    def retrieve(self, query, *args, **kwargs):
        """Return documents relevant to the query."""

        pass


class BaseGenerator(ABC):
    """
    Minimal contract for answer generation implementations.

    Concrete generators can wrap a local LLM, remote model, or test double
    without changing callers that depend on this interface.
    """

    @abstractmethod
    def generate(self, query, docs, *args, **kwargs):
        """Generate an answer for the query using the provided documents."""

        pass


class BaseReranker(ABC):
    """
    Minimal contract for reranking implementations.

    Concrete rerankers can use cross-encoders, heuristics, or other scoring
    strategies while preserving the same pipeline-level contract.
    """

    @abstractmethod
    def rerank(self, query, docs, *args, **kwargs):
        """Return documents reordered by relevance to the query."""

        pass
