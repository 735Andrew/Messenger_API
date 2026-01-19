from datetime import datetime

from pydantic import BaseModel, Field


class ChatCreationSchema(BaseModel):
    title: str = Field(min_length=1, max_length=200)


class ChatSchema(ChatCreationSchema):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
