from datetime import datetime

from pydantic import BaseModel


class PurchaseDTO(BaseModel):
    purchase_date: datetime
    item_id: int
    user_id: int

    class Config:
        from_attributes = True


class UpdateAddressDTO(BaseModel):
    delivery_address: str

    class Config:
        from_attributes = True


class PurchaseInDB(PurchaseDTO, UpdateAddressDTO):
    id: int

    class Config:
        from_attributes = True
