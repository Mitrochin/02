from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional


class UserSchema(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=6, max_length=8)


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class ContactSchema(BaseModel):
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    email: EmailStr
    phone: str = Field(pattern=r'^\+?1?\d{9,15}$', description="Номер телефону у міжнародному форматі")
    birthday: date = Field(description="Дата народження")
    data_add: Optional[str] = Field(max_length=250, description="Додаткові дані")


class ContactResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    birthday: date
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    user: Optional[UserResponse]
    data_add: Optional[str]

    class Config:
        from_attributes = True


