import jwt
from datetime import datetime, timedelta, timezone
from src.config import settings

def create_access_token(subject: str, minutes_expiration_time: int = 60*24) -> str:
    expiration_time = datetime.now(timezone.utc) + timedelta(minutes=minutes_expiration_time)
    to_encode = {"exp": expiration_time, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, settings.algorithm)

    return encoded_jwt
