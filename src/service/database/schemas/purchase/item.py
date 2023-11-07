from pydantic import BaseModel


class ItemDTO(BaseModel):
    id: int
    book_id: str
    amount_item: int

    class Config:
        orm_mode = True
