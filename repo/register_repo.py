from model.model import register
from fastapi import HTTPException
from sqlalchemy.orm import Session 
import auth.hashing as hashing
from database import get_db
from dto.schemas import register_schemas 


def register_details(request:register_schemas,db:Session):
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