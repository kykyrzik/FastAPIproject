from pydantic import BaseModel


class GenrDTO(BaseModel):
    id: int
    genre: str

    class Config:
        orm_mode = True
