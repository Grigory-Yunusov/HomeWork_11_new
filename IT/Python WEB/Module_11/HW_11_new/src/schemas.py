#schemas.py
from pydantic import BaseModel
from datetime import datetime, timedelta, date

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: date
    additional_data: str | None

class ContactCreate(ContactBase):
    pass

class ContactResponse(ContactBase):
    id: int

    class Config:
        from_attributes = True

