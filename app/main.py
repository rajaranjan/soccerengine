from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.PlayerRouter import PlayerRouter

app = FastAPI(title="Soccer Engine API", docs_url="/docs")

# Add the frontend origin to the allowed list
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}

app.include_router(PlayerRouter, prefix="/v1/players", tags=["Players"])
