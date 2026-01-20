from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func

from app.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    chat_id = Column(ForeignKey("chats.id"))
    text = Column(String, nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(), # set timestamp on the database side
        nullable=False,
    )
