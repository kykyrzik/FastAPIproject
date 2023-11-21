from fastapi import APIRouter

from src.api.v1.endpoints.user import user


router = APIRouter()

router.include_router(router=user.router, prefix="/user", tags=["Users"])
