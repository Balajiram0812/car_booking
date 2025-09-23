from fastapi import APIRouter,Depends,HTTPException
from schemas import login,Token
from sqlalchemy.orm import Session
from database import get_db
from model import register
from hashing import hash
from jwttoken import  create_access_token

router=APIRouter(tags=["auth"])

@router.post("/login")
def login(request: login, db: Session = Depends(get_db)):
    userlogin = db.query(register).filter(register.email == request.username).first()

    if not userlogin:
        raise HTTPException(status_code=404, detail="invalid credentials")

    if not hash.verify(userlogin.password, request.password):
        raise HTTPException(status_code=404, detail="invalid password")

    access_token = create_access_token(
        data={"sub": userlogin.email, "name": userlogin.first_name, "last_name":userlogin.last_name,"genter":userlogin.genter, "role":userlogin.role}
    )
    return Token(access_token=access_token, token_type="bearer")

