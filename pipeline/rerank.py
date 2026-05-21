from core.interfaces import BaseReranker
from retrieval.reranker import rerank_documents


class CrossEncoderReranker(BaseReranker):
    """Interface-compatible adapter for the existing CrossEncoder reranker."""

    def rerank(
        self,
        query,
        docs,
        top_k=4,
        *args,
        **kwargs,
    ):
        return rerank_documents_stage(
            query=query,
            documents=docs,
            top_k=top_k,
        )


def rerank_documents_stage(query, documents, top_k):
    """Rerank retrieved documents with the existing CrossEncoder reranker."""

    reranked_documents = rerank_documents(
        query=query,
        documents=documents,
        top_k=top_k,
    )

    return reranked_documents


def rerank(query, documents, top_k=4):
    """Backward-compatible alias for the rerank stage."""

    return rerank_documents_stage(
        query=query,
        documents=documents,
        top_k=top_k,
    )
