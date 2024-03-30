# models.py
from src.db.database import Base
from sqlalchemy import Column, Integer, String, Date

# Database model
class ContactDB(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String)
    birthday = Column(Date)
    additional_data = Column(String, nullable=True)


class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(255), nullable=False)


