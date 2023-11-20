from pydantic import BaseModel


class AuthorsDTO(BaseModel):
    id: int
    fullname_author: str

    class Config:
        orm_mode = True
