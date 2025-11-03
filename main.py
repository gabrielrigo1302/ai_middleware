from fastapi import FastAPI
from src.endpoints.controllers.SummaryController import router as summary_router

app = FastAPI(title="AI Middleware", version="1.0.0")

app.include_router(summary_router, prefix="/summary", tags=["Summary"])

@app.get("/status", tags=["Status"])
async def health():
    return {"status": "ok"}


