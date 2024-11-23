from .base import Base
from sqlalchemy import Column, Integer


class Song(Base):
    __tablename__ = "Songs"
    id = Column(Integer, primary_key=True, index=True)
    song_id = Column(Integer, Required=True)

