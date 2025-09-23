from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import register_schemas,register_responce
from model import register
import hashing 

router=APIRouter(
    tags=["register"]
    # prefix=""
)

@router.post("/register", response_model=register_responce)
def add_register_details(request:register_schemas,db:Session=Depends(get_db)):
    add_new=register(first_name=request.first_name,
                      last_name=request.last_name,
                      email=request.email,
                      password=hashing.hash.bcrypt(request.password),
                      role=request.role, 
                      genter=request.genter,
                      age=request.age
                      )
    if request.password==request.re_password:
        db.add(add_new)
        db.commit()
        db.refresh(add_new)
        return add_new
    
    else:
        raise HTTPException(status_code=404, detail="password and re-password miss matched")
