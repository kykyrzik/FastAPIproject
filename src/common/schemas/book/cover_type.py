from pydantic import BaseModel


class CoverTypeDTO(BaseModel):
    id: int
    cover_type: str

    class Config:
        orm_mode = True
