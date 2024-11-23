from .base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Music(Base):
    __tablename__ = "Music"
    music_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    #sound: Mapped[]
