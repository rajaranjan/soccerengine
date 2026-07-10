from fastapi import FastAPI
from app.routes.PlayerRouter import PlayerRouter

app = FastAPI(title="Soccer Engine API", docs_url="/docs")

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}

app.include_router(PlayerRouter, prefix="/v1/players", tags=["Players"])
