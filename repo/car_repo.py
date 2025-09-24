from dto.schemas import add_car
from fastapi import Depends
from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session      
from database import get_db
from model.model import CarDetails  

def create_car(request: add_car, db:Session):
    new_car = CarDetails(
        model_name=request.model_name,
        manufacture_year=request.manufacture_year,
        insurance_cover=request.insurance_cover,
        color=request.color,
        engine=request.engine,
        power=request.power,
        torque=request.torque,
        variant=request.variant,
        price=request.price,
        tax=request.tax
    )
    db.add(new_car)
    db.commit()
    db.refresh(new_car) 

    return new_car


