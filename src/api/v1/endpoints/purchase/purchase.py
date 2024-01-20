from typing import Any

from fastapi import APIRouter, Depends
from starlette.requests import Request

from src.services.database.repositories.purchase.item_repo import ItemRepo
from src.services.database.repositories.purchase.purchase_repo import PurchaseRepo
from src.services.cart.cart import Cart
from .create_purchase import create_purchase_DTO

router = APIRouter()


@router.post("/create_purchase/{user_id}")
async def create_purchase(request: Request,
                          user_id: int,
                          address: str,
                          item_crud: ItemRepo = Depends(),
                          purchase_crud: PurchaseRepo = Depends()
                          ) -> Any:
    cart = Cart(request)
    if len(cart) < 1:
        return {"detail": "There are no book in the cart"}
    values = cart.__dict__["cart"]
    total_price = cart.get_total_price()
    for book_id in values:
        item_id = (await item_crud.add_item(book_id=book_id,
                                            amount_item=values[book_id]["quality"]
                                            )).id
        await purchase_crud.add_purchase(create_purchase_DTO(total_price, item_id, user_id, address))
    cart.clear()
    return {"successes": True}


@router.get("/get")
async def get_purchase(purchase_id: int, crud: PurchaseRepo = Depends()) -> Any:
    return await crud.get_purchase(purchase_id)
