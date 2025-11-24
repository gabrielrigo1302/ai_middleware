from typing import List, Dict, Any
from src.db.vector import driver
from langchain_community.embeddings import HuggingFaceEmbeddings


async def get_rag_text_query_service(query: str, top_k: int = 1) -> Dict[str, Any]:
    rag = driver
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    # Gerar embedding para a query
    query_embedding = embedding_model.embed_query(query)

    relevant_chunks = []

    try:
        with rag.session() as session:
            result = session.run(
                """
                MATCH (c:Chunk)
                WITH c, 
                        gds.similarity.cosine(c.embedding, $query_embedding) AS similarity
                ORDER BY similarity DESC
                LIMIT $top_k
                RETURN c.content AS content, 
                        c.id AS chunk_id,
                        similarity
            """,
                {"query_embedding": query_embedding, "top_k": top_k},
            )

            relevant_chunks = [
                {
                    "content": record["content"],
                    "chunk_id": record["chunk_id"],
                    "similarity": record["similarity"],
                }
                for record in result
            ]

            if not relevant_chunks:
                not_found: List[str] = [
                    "Não encontrei informações relevantes nos documentos."
                ]

                return {"resposta": not_found, "pergunta": query}

            # Construir contexto
            context: List[dict[str, str]] = [
                {
                    "content": str(chunk["content"]),
                    "chunk_id": str(chunk["chunk_id"]),
                    "similarity": str(chunk["similarity"]),
                }
                for chunk in relevant_chunks
            ]

            response: Dict[str, Any] = {
                "content": str(context[0]["content"]),
                "chunk_id": str(context[0]["chunk_id"]),
                "similarity": str(context[0]["similarity"]),
                "pergunta": query,
            }

            return response

    finally:
        rag.close()
