from pydantic import BaseModel


class RARDDTO(BaseModel):
    id: int
    rating: str

    class Config:
        orm_mode = True
