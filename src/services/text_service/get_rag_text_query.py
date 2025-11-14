from typing import List, Dict, Any
from src.db import graph_store
from langchain_community.embeddings import HuggingFaceEmbeddings

async def get_rag_text_query(query: str) -> Dict[str, Any]:
    rag = graph_store.driver
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
     # Gerar embedding para a query
    query_embedding = embedding_model.embed_query(query)
    
    relevant_chunks = []

    try:
        with rag.session() as session:
            result = session.run("""
                MATCH (c:Chunk)
                WITH c, 
                        gds.similarity.cosine(c.embedding, $query_embedding) AS similarity
                ORDER BY similarity DESC
                LIMIT $top_k
                RETURN c.content AS content, 
                        c.id AS chunk_id,
                        similarity
            """, {
                'query_embedding': query_embedding,
                'top_k': 3
            })
        
            relevant_chunks = [{
                'content': record['content'],
                'chunk_id': record['chunk_id'],
                'similarity': record['similarity']
            } for record in result]

            if not relevant_chunks:
                not_found: List[str] = ["Não encontrei informações relevantes nos documentos."]
                
                return {
                    "resposta": not_found,
                    "pergunta": query
                }
            
            # Construir contexto
            context: List[str] = [
                f"Documento {chunk['chunk_id']} (similaridade: {chunk['similarity']:.3f}):\n{chunk['content']}"
                for chunk in relevant_chunks
            ]
            
            response: Dict[str, Any] = {
                "resposta": context,
                "pergunta": query
            }
            
            return response
        
    finally:
        rag.close()