from datetime import datetime

from pydantic import BaseModel


class PurchaseDTO(BaseModel):
    id: int
    delivary_address: str
    purchase_date: datetime
    item_id: int
    user_id: int

    class Config:
        orm_mode = True
