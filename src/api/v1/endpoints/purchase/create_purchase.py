from datetime import datetime

from src.common.schemas.purchase.purchase import PurchaseCreateDTO


def create_purchase_DTO(total_price, item_id, user_id, address) -> PurchaseCreateDTO:
    return PurchaseCreateDTO(price=total_price,
                             item_id=item_id,
                             user_id=user_id,
                             delivery_address=address,
                             purchase_date=datetime.now()
                             )
