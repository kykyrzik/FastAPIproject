from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm


from src.services.database.repositories.user.user_repositories import UserRepositories
from src.services.security.jwt import decode_access_token

router = APIRouter(tags=["Login"])


@router.post("/token")
async def login_access_token(crud: UserRepositories = Depends(),
                             form_data: OAuth2PasswordRequestForm = Depends()
                             ) -> dict[str, str]:
    return await crud.authenticate(email=form_data. username,  # username - username or email
                                   password=form_data.password)


@router.get('/register/{token}')
async def activate_user(token: str,
                        crud: UserRepositories = Depends()
                        ) -> dict[str, bool | str]:
    data_in_token = decode_access_token(token)

    if not data_in_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could not validate credentials",
                            headers={"WWW-Authenticate": "Bearer"}
                            )
    user = await crud.get(email=data_in_token.get("sub").get('email'))
    if user:
        await crud.activate_user(user_id=user.id)
        return {"success": True,
                'detail': f'User {user.username} has registered by email: {user.email} '}
    raise HTTPException(status_code=404, detail='Registration time expired')
