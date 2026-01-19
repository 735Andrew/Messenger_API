from fastapi import HTTPException, status

from app.chats.service import ChatService
from app.chats.schemas import ChatSchema


async def check_id(id: int) -> ChatSchema:
    chat = await ChatService.get_one(id)

    if chat is None:
        raise HTTPException(
            detail=f"There is no chat with id <{id}>",
            status_code=status.HTTP_404_NOT_FOUND,
        )

    return chat
