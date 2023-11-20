from pydantic import BaseModel


class CoverTypeDTO(BaseModel):
    id: int
    cover_type: str

    class Config:
        from_attributes = True
