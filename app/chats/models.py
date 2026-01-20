from sqlalchemy import Column, Integer, String, DateTime, func

from app.database import Base


class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(), # set timestamp on the database side
        nullable=False,
    )
