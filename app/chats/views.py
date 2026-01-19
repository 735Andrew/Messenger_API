from fastapi import APIRouter, Query, status, Response, Depends

from app.chats.service import ChatService
from app.chats.schemas import ChatCreationSchema, ChatSchema
from app.messages.service import MessageService
from app.messages.schemas import MessageCreationSchema, MessageSchema
from app.chats.dependencies import check_id


router = APIRouter(prefix="/chats")


@router.post("", response_model=ChatSchema)
async def chat_create(chat_data: ChatCreationSchema):
    title = chat_data.title.strip()
    return await ChatService.create_chat(title=title)


@router.post("/{id}/messages", response_model=MessageSchema)
async def send_message(
    message_data: MessageCreationSchema,
    chat: ChatSchema = Depends(check_id),
):
    return await MessageService.create_message(chat_id=chat.id, text=message_data.text)


@router.get("/{id}", response_model=dict())
async def take_messages(
    limit: int = Query(default=20, gt=0, lt=100),
    chat: ChatSchema = Depends(check_id),
):

    report = {
        "Chat": await ChatService.get_one(chat.id),
        "Messages": await MessageService.take_messages(chat_id=chat.id, limit=limit),
    }

    return report


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_chat(chat: ChatSchema = Depends(check_id)):

    await MessageService.delete_messages(chat.id)
    await ChatService.delete_chat(chat.id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
