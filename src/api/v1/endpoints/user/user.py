from typing import Any

from fastapi import APIRouter, Depends, HTTPException

from src.common.schemas.user.user import UserCreateDTO, UpdateUsername
from src.services.database.repositories.user.user_repositories import UserRepositories


router = APIRouter()


@router.post('/create/')
async def user_create(user: UserCreateDTO,
                      crud: UserRepositories = Depends()
                      ) -> Any:
    result = await crud.create_user(user)
    return {'result': result,
            'message': 'confirm'}


@router.patch('/update/{user_id}')
async def update_user(user_id: int,
                      data: UpdateUsername,
                      crud: UserRepositories = Depends()
                      ) -> Any:

    return await crud.update_user(user_id=user_id, data=data)


@router.delete('/delete/{user_id}')
async def delete_user(user_id: int,
                      crud: UserRepositories = Depends(UserRepositories)
                      ) -> dict[str, str]:

    result = await crud.delete_user(user_id=user_id)
    if result:
        return {'message': "success"}
    raise HTTPException(status_code=404, detail="user does not exists")
