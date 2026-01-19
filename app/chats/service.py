from sqlalchemy import select, insert, delete

from app.database import async_session_maker
from app.chats.models import Chat
from app.chats.schemas import ChatSchema


class ChatService:

    @classmethod
    async def get_one(cls, chat_id: int) -> ChatSchema:
        async with async_session_maker() as session:
            query = select(Chat).filter_by(id=chat_id)
            chat = await session.execute(query)
            return chat.scalar_one_or_none()

    @classmethod
    async def create_chat(cls, **data) -> ChatSchema:
        async with async_session_maker() as session:
            query = insert(Chat).values(**data).returning(Chat)
            data = await session.execute(query)
            chat_id = data.scalar_one().id
            await session.commit()
            return await ChatService.get_one(chat_id)

    @classmethod
    async def delete_chat(cls, chat_id: int) -> None:
        async with async_session_maker() as session:
            query = delete(Chat).filter_by(id=chat_id)
            await session.execute(query)
            await session.commit()
