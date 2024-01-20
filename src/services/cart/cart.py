from decimal import Decimal

from starlette.requests import Request

from src.common.schemas.book.book import BookDTO


class Cart:
    def __init__(self, request: Request):
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, book: BookDTO, quality: int = 1, update_quantity=False) -> None:
        book_id = book.ISBN
        if book_id not in self.cart:
            self.cart[book_id] = {"quality": 0, "price": str(book.unit_price), "name": book.name_book}
        if update_quantity:
            self.cart[book_id]["quality"] = quality
        else:
            self.cart[book_id]["quality"] += quality

    def remove(self, book_id: str):
        del self.cart[book_id]

    def get_total_price(self):
        return sum(Decimal(item["price"]) * Decimal(item["quality"])
                   for item in self.cart.values()
                   )

    def clear(self):
        del self.session["cart"]

    def __len__(self):
        return sum(item["quality"] for item in self.cart.values())
