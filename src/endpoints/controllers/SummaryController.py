from fastapi import APIRouter
from src.endpoints.models.SummaryModel import SummarizeResponse, SummarizeRequest
from src.endpoints.services.SummaryService import SummaryService;

router = APIRouter()

# @router.post("/summarize", response_model=SummarizeResponse, dependencies=[Depends(gateway_protect)])
@router.post("/summarize", response_model=SummarizeResponse)
async def summarize(req: SummarizeRequest):
    service = SummaryService()
    summary = await service.summarize(req.conversation_id, req.max_tokens)
    return SummarizeResponse(summary=summary)