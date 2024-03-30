#models.user.py
from src.db.database import Base
from sqlalchemy import Column, Integer, String


class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(255), nullable=False)


    