from datetime import timedelta, datetime

from jose import jwt

from src.config.setting import load_settings

ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, load_settings().SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_useful_data_in_token(token: str) -> dict | None:
    try:
        decode_token = jwt.get_unverified_claims(token)
        return decode_token
    except jwt.JWTError:
        return None
