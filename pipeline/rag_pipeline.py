from pipeline.rewrite import rewrite_query
from pipeline.retrieve import retrieve_documents
from pipeline.rerank import rerank_documents_stage
from pipeline.refine import refine_documents, score_confidence
from pipeline.insert import insert_context
from pipeline.generate import generate_answer_stage


def run_rag_pipeline(
    query,
    vector_store,
    chunks,
    top_k,
    chat_history=None,
):
    """
    Run the backend RAG stages without handling any Streamlit UI.

    Stage order:
    Rewrite -> Retrieve -> Rerank -> Refine -> Insert -> Generate
    """

    # 1. Rewrite
    rewritten_query = rewrite_query(
        query=query,
        chat_history=chat_history,
    )

    # 2. Retrieve
    retrieved_docs = retrieve_documents(
        query=rewritten_query,
        vector_store=vector_store,
        chunks=chunks,
        top_k=top_k,
    )

    if not retrieved_docs:
        return {
            "answer": "No relevant information found in uploaded documents.",
            "retrieval_query": rewritten_query,
            "rewritten_query": rewritten_query,
            "retrieved_docs": [],
            "reranked_docs": [],
            "refined_docs": [],
            "inserted_context": [],
            "final_docs": [],
            "confidence": 0,
        }

    # 3. Rerank
    reranked_docs = rerank_documents_stage(
        query=rewritten_query,
        documents=retrieved_docs,
        top_k=top_k,
    )

    # 4. Refine
    refined_docs = refine_documents(
        documents=reranked_docs,
        top_k=top_k,
    )

    # 5. Insert
    inserted_context = insert_context(
        documents=refined_docs,
    )

    # Confidence remains on the final document set consumed by existing app.py.
    confidence = score_confidence(
        documents=inserted_context,
        question=query,
    )

    # 6. Generate
    final_answer = generate_answer_stage(
        question=query,
        documents=inserted_context,
    )

    return {
        "answer": final_answer,
        "final_answer": final_answer,
        "retrieval_query": rewritten_query,
        "rewritten_query": rewritten_query,
        "retrieved_docs": retrieved_docs,
        "reranked_docs": reranked_docs,
        "refined_docs": refined_docs,
        "inserted_context": inserted_context,
        "final_docs": inserted_context,
        "confidence": confidence,
    }
