from datetime import datetime

from pydantic import BaseModel, Field


class MessageCreationSchema(BaseModel):
    text: str = Field(min_length=1, max_length=5000)


class MessageSchema(MessageCreationSchema):
    id: int
    chat_id: int
    created_at: datetime

    class Config:
        from_attributes = True
