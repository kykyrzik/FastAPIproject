import re
from pydantic import BaseModel, EmailStr, Field, field_validator


class ValidationPassword(BaseModel):
    password: str

    @field_validator("password")
    @classmethod
    def validate_by_regexp(cls, password: str) -> str:
        pattern = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&._])[A-Za-z\d@$!%*#?&._]{8,}$'
        if len(password) == 60:  # he's valid
            return password
        if re.match(pattern, password) is None:
            raise ValueError('Password has incorrect format.')
        return password


class UserBase(BaseModel):
    email: EmailStr = Field(title="Enter the email")
    username: str = Field(title="Enter the username")


class UserCreateDTO(UserBase, ValidationPassword):
    class Config:
        from_attributes = True


class UserInDB(UserCreateDTO):
    id: int
    is_admin: bool | None
    is_active: bool | None

    class Config:
        from_attributes = True


class UpdateUsername(BaseModel):
    """How swap password used class validation"""
    username: str

    class Config:
        from_attributes = True
