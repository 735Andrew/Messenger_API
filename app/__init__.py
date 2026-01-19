from fastapi import FastAPI
from app.chats.views import router

app = FastAPI()

app.include_router(router)
