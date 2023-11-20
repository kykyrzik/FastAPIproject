from pydantic import BaseModel


class GenreDTO(BaseModel):
    id: int
    genre: str

    class Config:
        from_attributes = True
