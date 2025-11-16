import os
from typing import Any, Dict, List
from fastapi import HTTPException, status
from neo4j import Driver
from src.utils.logger_debug import LogLevel, log_debug
from src.db.graph import graph_store
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

async def post_rag_text_add_document() -> str:
    rag_driver = graph_store.driver
    
    try:
        ### Criar SCHEMA 
        await create_schema(rag_driver)

        ### Ler Documentos
        documents = await read_documents()

        ### Dividir em chunks
        chunks = chunk_splitter(documents)

        ### Criar embeddings
        chunks = await embedding_generator(chunks)

        ### Inserir no Neo4j
        await add_document_to_graph(rag_driver, chunks)

        return "Documentos adicionados com sucesso à base de grafos."

    except Exception:
        log_debug(LogLevel.error, "Mistral Provider", "Erro ao comunicar com o provedor Mistral.")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=Exception)
    
    finally:
        rag_driver.close()

async def create_schema(driver: Driver) -> None:
   with driver.session() as session:
        # Criar constraints para garantir unicidade
        session.run("""
            CREATE CONSTRAINT document_id IF NOT EXISTS 
            FOR (d:Document) REQUIRE d.id IS UNIQUE
        """)
        
        session.run("""
            CREATE CONSTRAINT chunk_id IF NOT EXISTS 
            FOR (c:Chunk) REQUIRE c.id IS UNIQUE
        """)

async def read_documents() -> List[Dict[str, str]]:

    folder_path = r"C:\Users\gabri\Documents\AI\ai_middleware\data"
    documents: List[Dict[str, str]] = []

    if not os.path.isdir(folder_path):
        log_debug(LogLevel.warning, "read_documents", f"Data folder not found: {folder_path}")
        return documents

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    documents.append({
                        'filename': filename,
                        'content': content,
                        'file_path': file_path,
                    })
            except Exception as e:
                # Log and skip files that cannot be read
                log_debug(LogLevel.error, "read_documents", f"Failed to read {file_path}: {e}")

    return documents

def chunk_splitter(documents: List[Dict[str, str]]) -> List[Dict[str, str]]:
    text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        
    chunks: List[Dict[str, Any]] = []
    for doc in documents: # type: ignore
        doc_chunks = text_splitter.split_text(doc['content']) # type: ignore
        for i, chunk in enumerate(doc_chunks):
            chunks.append({ # type: ignore
                'filename': doc['filename'],
                'content': chunk,
                'chunk_id': i,
                'file_path': doc['file_path']
            })
    
    return chunks

async def embedding_generator(chunks: List[Dict[str, str]]) -> List[Dict[str, str]]:
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    ### Criar embeddings
    texts = [chunk['content'] for chunk in chunks] # type: ignore
    embeddings = embedding_model.embed_documents(texts) # type: ignore
    
    for i, chunk in enumerate(chunks): # type: ignore
        chunk['embedding'] = embeddings[i] # type: ignore
    
    return chunks

async def add_document_to_graph(driver: Driver, chunks: List[Dict[str, str]]) -> None:
    with driver.session() as session:
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