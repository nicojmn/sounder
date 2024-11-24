from typing import Required
from .base import Base
from sqlalchemy import Column, Integer

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, Required=True)
