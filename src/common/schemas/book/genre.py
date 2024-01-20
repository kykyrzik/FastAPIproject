from pydantic import BaseModel


class GenreDTO(BaseModel):
    genre: str

    class Config:
        from_attributes = True


class GenreInDB(GenreDTO):
    id: int
