import re
from fastapi import status
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.base import Base
from models.liked_song import LikedSong
from models.user import User
from models.song import Song


class Database:

    def __init__(self) -> None:
        self.engine = create_engine("sqlite://", echo=True)
        self.conn = self.engine.connect()

    def __del__(self) -> None:
        self.conn.close()
        self.engine.dispose()

    def create_tables(self) -> None:
        Base.metadata.create_all(self.engine)
        LikedSong.metadata.create_all(self.engine)
        User.metadata.create_all(self.engine)
        Song.metadata.create_all(self.engine)

    def drop_tables(self) -> None:
        Base.metadata.drop_all(self.engine)
        LikedSong.metadata.drop_all(self.engine)
        User.metadata.drop_all(self.engine)
        Song.metadata.drop_all(self.engine)

    
    def add_user(self, user_id: int) -> None:
        with Session(self.engine) as session:
            if not session.query(User).filter(User.user_id == user_id).first():
                user = User(user_id=user_id)
                session.add(user)
                session.commit()

    def add_song(self, song_id: int) -> None:
        with Session(self.engine) as session:
            if not session.query(Song).filter(Song.song_id == song_id).first():
                song = Song(song_id=song_id)
                session.add(song)
                session.commit()

    def add_liked_song(self, user_id: int, song_id: int) -> None:
        with Session(self.engine) as session:
            if not session.query(LikedSong).filter(LikedSong.user_id == user_id, LikedSong.song_id == song_id).first():
                liked_song = LikedSong(user_id=user_id, song_id=song_id)
                session.add(liked_song)
                session.commit()