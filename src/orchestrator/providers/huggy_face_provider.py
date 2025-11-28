from fastapi import HTTPException, status
from typing import List
from src.types.enums.log_enums import LogLevelEnum
from src.utils.logger_debug import log_debug
from langchain_community.embeddings import HuggingFaceEmbeddings


async def huggy_face_text_embedding_documents_provider(
    content: List[str],
) -> List[List[float]]:
    try:
        embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        # Gerar embedding para a query
        return embedding_model.embed_documents(content)
    except Exception:
        log_debug(
            LogLevelEnum.error,
            "Mistral Provider",
            "Erro ao comunicar com o provedor Mistral.",
        )
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=Exception)


async def huggy_face_text_embedding_query_provider(content: str) -> List[float]:
    try:
        embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        # Gerar embedding para a query
        return embedding_model.embed_query(content)
    except Exception:
        log_debug(
            LogLevelEnum.error,
            "Mistral Provider",
            "Erro ao comunicar com o provedor Mistral.",
        )
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=Exception)
