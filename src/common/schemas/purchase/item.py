from pydantic import BaseModel


class BaseItem(BaseModel):
    book_id: str
    amount_item: int

    class Config:
        orm_mode = True


class ItemDTO(BaseItem):
    id: int

    class Config:
        orm_mode = True