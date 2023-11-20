import re
from pydantic import BaseModel, EmailStr, Field, field_validator


class ValidationPassword(BaseModel):
    password: str = Field(...)

    @field_validator("password")
    @classmethod
    def validate_by_regexp(cls, password: str) -> str:
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
        if re.match(pattern, password) is None:
            raise ValueError('Password has incorrecr format.')
        return password


class UserBase(BaseModel):
    email: EmailStr = Field(title="Enter the email")
    username: str = Field(title="Enter the username")


class UserCreateDTO(UserBase, ValidationPassword):
    class Config:
        orm_mode = True


class UpdateUsername(BaseModel):
    """How swap password used class validation"""
    username: str

    class Config:
        orm_mode = True
