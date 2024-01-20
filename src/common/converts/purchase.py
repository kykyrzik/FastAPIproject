from src.services.database.models.purchase.purchase import Purchase
from src.common.schemas.purchase.purchase import PurchaseInDB


def convert_purchase_model_to_dto(purchase: Purchase) -> PurchaseInDB:
    return PurchaseInDB(id=purchase.id,
                        item_id=purchase.id,
                        price=purchase.price,
                        purchase_date=purchase.purchase_date,
                        delivery_address=purchase.delivery_address,
                        user_id=purchase.user_id)
