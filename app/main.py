from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import agent_assistant

app = FastAPI()

app.include_router(agent_assistant.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root() -> dict:
    return {"Hello": "World"}


@app.get("/health_check")
def health_check() -> bool:
    return True



