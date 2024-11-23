from typing import Required
from .base import Base
from sqlalchemy import Column, Integer, ForeignKey


class LikedSong(Base):
    __tablename__ = "Liked Songs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), Required=True)
    song_id = Column(Integer, ForeignKey("songs.song_id"), Required=True)

