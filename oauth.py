from fastapi import Depends, HTTPException,status
import jwttoken
from model import register
from fastapi.security import OAuth2PasswordBearer
# from jose import JWTError
from schemas import TokenData
from database import SessionLocal,engine
from jwttoken import verify_tokken,jwt,SECRET_KEY, ALGORITHM


session = SessionLocal(bind=engine)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    print(f"token data: {token}" )
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    print(F"payload in data : {payload}")
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_data = verify_tokken(token, credentials_exception)

    print(f"Decoded token data: {token_data}")

    users= session.query(register).filter(register.email== token_data.username).first()
    print (f"users details in printed : {users.role}")

    if register is None:
        raise credentials_exception  
    
    return users

def role_checker(required_roles: list[str]):
    def wrapper(current_user: dict = Depends(get_current_user)):
        if current_user.role not in required_roles:
            raise HTTPException(
                status_code=403,
                detail="You do not have enough permissions"
            )
        return current_user
    
    return wrapper