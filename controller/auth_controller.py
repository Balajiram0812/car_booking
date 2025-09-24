from fastapi import APIRouter,Depends,HTTPException
from dto.schemas import login,Token
from sqlalchemy.orm import Session
from database import get_db
from model.model import register
from auth.hashing import hash
from auth.jwttoken import  create_access_token
from repo.auth_repo import login_user

router=APIRouter(tags=["auth"])

@router.post("/login")
def login(request: login, db: Session = Depends(get_db)):
    return login_user(request,db)

    

