from typing import List
from fastapi import HTTPException, status
from settings import settings
from src.utils.logger_debug import log_debug, LogLevel
from mistralai import Mistral

if settings.MISTRAL_KEY:
    client = Mistral(api_key=settings.MISTRAL_KEY)
else:
    log_debug(LogLevel.warning, "Mistral Provider", "Nenhuma chave de API Mistral configurada.")
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Nenhuma chave de API Mistral configurada.")

async def mistral_text_to_text_provider(prompt: str) -> str:
    try:
        chat_response = client.chat.complete(
            model="mistral-small-latest",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return chat_response.choices[0].message.content
    except Exception:
        log_debug(LogLevel.error, "Mistral Provider", "Nenhuma chave de API Mistral configurada.")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Erro ao comunicar com o provedor Mistral")

async def mistral_text_embedding_provider(content: List[str]) -> List[float]:
    try:
        embedding_response = client.embeddings.create(
            model="mistral-embed",
            inputs=content,
        )
       
        # log_debug(LogLevel.info, "Mistral Provider", embedding_response.data[0].embedding)

        return embedding_response.data[0].embedding
    except Exception:
        log_debug(LogLevel.error, "Mistral Provider", "Erro ao comunicar com o provedor Mistral.")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=Exception)