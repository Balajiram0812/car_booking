from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from dto.schemas import register_schemas,register_responce
from model.model import register
import auth.hashing as hashing 
from repo.register_repo import register_details


router=APIRouter(
    tags=["register"]
    # prefix=""
)

@router.post("/register", response_model=register_responce)
def add_register_details(request:register_schemas,db:Session=Depends(get_db)):
    return register_details(request,db)
    
    