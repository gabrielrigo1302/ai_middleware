from fastapi import FastAPI
from src.routes import routers

app = FastAPI(title="AI Middleware", version="1.0.0")

for router in routers:
    app.include_router(router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
