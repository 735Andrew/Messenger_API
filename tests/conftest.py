import json

import pytest
from sqlalchemy import insert
from httpx import AsyncClient, ASGITransport

from app import app as fastapi_app
from app.database import Base, async_session_maker, engine
from app.chats.models import Chat
from app.messages.models import Message


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f"tests/mock_{model}.json", "r") as file:
            return json.load(file)

    chats = open_mock_json("chats")
    messages = open_mock_json("messages")

    async with async_session_maker() as session:
        add_chats = insert(Chat).values(chats)
        add_messages = insert(Message).values(messages)

        await session.execute(add_chats)
        await session.execute(add_messages)

        await session.commit()


@pytest.fixture(scope="session")
async def ac():
    transport = ASGITransport(app=fastapi_app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
