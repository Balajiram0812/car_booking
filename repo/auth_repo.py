from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from model.model import register
from auth.hashing import hash       
from auth.jwttoken import create_access_token
from dto.schemas import Token   



def login_user(request,db):
    userlogin = db.query(register).filter(register.email == request.username).first()

    if not userlogin:
        raise HTTPException(status_code=404, detail="invalid credentials")

    if not hash.verify(userlogin.password, request.password):
        raise HTTPException(status_code=404, detail="invalid password")

    access_token = create_access_token(
        data={"sub": userlogin.email, "name": userlogin.first_name, "last_name":userlogin.last_name,"genter":userlogin.genter, "role":userlogin.role}
    )
    return Token(access_token=access_token, token_type="bearer")