from pydantic import BaseModel


class GenreDTO(BaseModel):
    id: int
    genre: str

    class Config:
        orm_mode = True
