from fastapi import APIRouter

from src.api.v1.endpoints.user import user
from src.api.v1.endpoints.book import book
from src.api.v1.endpoints.book import author

router = APIRouter()

router.include_router(router=user.router, prefix="/user", tags=["Users"])
router.include_router(router=book.router, prefix="/book", tags=["Book"])
router.include_router(router=author.router, prefix="/author", tags=["Author"])
