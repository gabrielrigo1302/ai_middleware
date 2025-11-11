import os
from typing import List, Dict, Any
from fastapi import HTTPException, status
from src.utils.logger_debug import LogLevel, log_debug
from ..orchestrator import orchestrator
from ..db import graph_store
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

async def get_summarized_text(text: str) -> str:
    return await orchestrator.text_to_text_orchestration(text)

async def get_text_embedding(content: List[str]) -> List[float]:
    return await orchestrator.text_embedding_orchestration(content)

async def post_rag_text_add_document(doc_id: str, text: str) -> str:
    rag = graph_store.driver
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    try:
        ### Criar SCHEMA 
        with rag.session() as session:
            # Criar constraints para garantir unicidade
            session.run("""
                CREATE CONSTRAINT document_id IF NOT EXISTS 
                FOR (d:Document) REQUIRE d.id IS UNIQUE
            """)
            
            session.run("""
                CREATE CONSTRAINT chunk_id IF NOT EXISTS 
                FOR (c:Chunk) REQUIRE c.id IS UNIQUE
            """)
        ### Criar Schema

        ### Ler Documentos
        folder_path = r"C:\Users\gabri\Documents\AI\ai_middleware\data"
        documents = []
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    documents.append({ # type: ignore
                        'filename': filename,
                        'content': content,
                        'file_path': file_path
                        })
        ### Ler Documentos

        ### Dividir em chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        
        chunks = []
        for doc in documents: # type: ignore
            doc_chunks = text_splitter.split_text(doc['content']) # type: ignore
            for i, chunk in enumerate(doc_chunks):
                chunks.append({ # type: ignore
                    'filename': doc['filename'],
                    'content': chunk,
                    'chunk_id': i,
                    'file_path': doc['file_path']
                })
        ### Dividir em chunks

        ### Criar embeddings
        texts = [chunk['content'] for chunk in chunks] # type: ignore
        embeddings = embedding_model.embed_documents(texts) # type: ignore
        
        for i, chunk in enumerate(chunks): # type: ignore
            chunk['embedding'] = embeddings[i] # type: ignore
        ### Criar embeddings

        ### Inserir no Neo4j
        with rag.session() as session:
            # Inserir documentos e chunks
            for chunk in chunks: # type: ignore
                # Inserir ou obter documento
                session.run("""
                    MERGE (d:Document {id: $filename})
                    SET d.file_path = $file_path,
                        d.created_at = datetime()
                """, {
                    'filename': chunk['filename'],
                    'file_path': chunk['file_path']
                })
                
                # Criar ID único para o chunk
                chunk_id = f"{chunk['filename']}_chunk_{chunk['chunk_id']}"
                
                # Inserir chunk com embedding
                session.run("""
                    MERGE (c:Chunk {id: $chunk_id})
                    SET c.content = $content,
                        c.chunk_index = $chunk_id_num,
                        c.embedding = $embedding,
                        c.created_at = datetime()
                    
                    WITH c
                    MATCH (d:Document {id: $filename})
                    MERGE (d)-[:CONTAINS]->(c)
                """, {
                    'chunk_id': chunk_id,
                    'chunk_id_num': chunk['chunk_id'],
                    'content': chunk['content'],
                    'embedding': chunk['embedding'],
                    'filename': chunk['filename']
                })
        ### Inserir no Neo4j

        return f"Documento {doc_id} adicionado com sucesso ao RAG."

    except Exception:
        log_debug(LogLevel.error, "Mistral Provider", "Erro ao comunicar com o provedor Mistral.")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=Exception)
    
    finally:
        rag.close()

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