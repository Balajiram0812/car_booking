from datetime import timedelta,datetime,timezone
from jose import jwt,JWTError
from fastapi import HTTPException
from dto.schemas import TokenData

SECRET_KEY = "f5a7296ca7af6463de48572ac11b0d1f4cac7e530aeca1ba1b863f76e2b68361"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_tokken(token: str, credentials_exception: HTTPException):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print ( f"verify token data : {payload}")
        email: str = payload.get("sub")
        role:str = payload.get("role")

        if email is None or role is None:
            raise credentials_exception
        return TokenData(username = email, role = role)
    
    except JWTError as e:
        raise credentials_exception