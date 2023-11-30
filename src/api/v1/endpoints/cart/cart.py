from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from starlette.requests import Request

from src.services.cart.cart import Cart
from src.services.database.repositories.book.book_repo import BookRepo


router = APIRouter()


@router.post("/add")
async def cart_add(request: Request,
                   book_id: str,
                   quantity: int = 1,
                   crud: BookRepo = Depends()) -> dict[str, bool]:
    try:
        cart = Cart(request)
        book = await crud.get_book(book_id)
        cart.add(book=book, quality=int(quantity), update_quantity=False)
        return {"successes": True}
    except AttributeError:
        raise HTTPException(
            status_code=404, detail=f"There isn't entry with id={book_id}"
        )


@router.get("/get")
async def get_cart(request: Request) -> dict[str, Any]:
    cart = Cart(request)
    values = cart.__dict__["cart"]
    quantity = cart.__len__()
    return {"quantity": quantity, "item": values}


@router.delete("/del")
async def cart_delete(request: Request, book_id: str):
    try:
        cart = Cart(request)
        cart.remove(book_id)
        return {"successes": True}
    except AttributeError:
        raise HTTPException(status_code=404, detail=f"There is no book with id={book_id} in the cart")


