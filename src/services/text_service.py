from typing import List
from ..orchestrator import orchestrator
from ..db import graph_store

async def get_summarized_text(text: str) -> str:
    return await orchestrator.text_to_text_orchestration(text)

async def get_text_embedding(content: List[str]) -> List[float]:
    return await orchestrator.text_embedding_orchestration(content)

async def post_rag_text_add_document(doc_id: str, text: str, metadata: dict = None) -> str:
    with graph_store.driver.session() as session:
        session.run(
                """
                MERGE (d:Document {id: $id})
                SET d.text = $text,
                    d.embedding = $embedding,
                    d.metadata = $metadata
                """,
                id=doc_id, text=text, embedding=get_text_embedding([text]), metadata=metadata
            )

    return "RAG text retrieval not yet implemented."