from fastapi import APIRouter

from src.api.v1.endpoints.user import user
from src.api.v1.endpoints.book import book
from src.api.v1.endpoints.book import author
from src.api.v1.endpoints.book import genre
from src.api.v1.endpoints.purchase import purchase
from src.api.v1.endpoints.cart import cart
from src.api.v1.endpoints.login import login

router = APIRouter()

router.include_router(router=user.router, prefix="/user", tags=["Users"])
router.include_router(router=book.router, prefix="/book", tags=["Book"])
router.include_router(router=author.router, prefix="/author", tags=["Author"])
router.include_router(router=genre.router, prefix="/genre", tags=["Genre"])
router.include_router(router=purchase.router, prefix="/purchase", tags=["purchase"])
router.include_router(router=cart.router, prefix="/cart", tags=["Cart"])
router.include_router(router=login.router, prefix="/login")
