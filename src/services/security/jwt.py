from datetime import timedelta, datetime

import jwt
from jwt import ExpiredSignatureError

from src.config.setting import load_auth_jwt


auth_jwt = load_auth_jwt()


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode,
                             auth_jwt.private_key_path.read_text(),
                             algorithm=auth_jwt.ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str | bytes) -> dict | None:
    try:
        decode_token = jwt.decode(token,
                                  auth_jwt.public_key_path.read_text(),
                                  algorithms=[auth_jwt.ALGORITHM])
        return decode_token
    except ExpiredSignatureError:
        return None
