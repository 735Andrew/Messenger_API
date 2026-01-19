from sqlalchemy import select, insert, delete

from app.database import async_session_maker
from app.messages.models import Message
from app.messages.schemas import MessageSchema


class MessageService:

    @classmethod
    async def create_message(cls, **data) -> MessageSchema:
        async with async_session_maker() as session:
            query = insert(Message).values(**data).returning(Message)
            message = await session.execute(query)
            await session.commit()
            return message.scalar()

    @classmethod
    async def take_messages(cls, chat_id: int, limit: int) -> [MessageSchema]:
        async with async_session_maker() as session:
            query = (
                select(Message.__table__.columns)
                .filter_by(chat_id=chat_id)
                .order_by(Message.created_at)
                .limit(limit)
            )

            chats = await session.execute(query)

            return chats.mappings().all()

    @classmethod
    async def delete_messages(cls, chat_id: int) -> None:
        async with async_session_maker() as session:
            query = (delete(Message).filter_by(chat_id=chat_id))
            await session.execute(query)
            await session.commit()
