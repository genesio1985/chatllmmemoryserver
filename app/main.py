from fastapi import FastAPI
from app.api.v1.endpoints.health import router as health_router

app=FastAPI(title="Chat LLM Memory Server",version="0.1.0")

app.include_router(health_router,prefix="/api/v1")

@app.get("/")
def root():
    return {"project":"CLMS","status":"running","version":"0.1.0"}
