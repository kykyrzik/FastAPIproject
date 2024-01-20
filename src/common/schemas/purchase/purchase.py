from datetime import datetime

from pydantic import BaseModel, condecimal


class PurchaseDTO(BaseModel):
    purchase_date: datetime
    item_id: int
    user_id: int
    price: condecimal(max_digits=8)

    class Config:
        from_attributes = True


class UpdateAddressDTO(BaseModel):
    delivery_address: str

    class Config:
        from_attributes = True


class PurchaseCreateDTO(PurchaseDTO, UpdateAddressDTO):
    class Config:
        from_attribute = True


class PurchaseInDB(PurchaseDTO, UpdateAddressDTO):
    id: int

    class Config:
        from_attributes = True
