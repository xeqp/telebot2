from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import ARRAY
from TZ1_TZ2.database.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    telegram_user_id = Column(String, unique=True, index=True)
    thread_id = Column(String, nullable=True)
    values = Column(ARRAY(String), default=list)
