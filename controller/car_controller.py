from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from database import get_db
from model.model import CarDetails
from dto.schemas import add_car
from auth.oauth import get_current_user,role_checker
from repo.car_repo import create_car

router=APIRouter(
    tags=["Car"],
    prefix="/car_detais"
    )

@router.post("/add", status_code=status.HTTP_201_CREATED)
def add_car_details(request: add_car, db:Session=Depends(get_db),  current_user: dict = Depends((role_checker(["admin"])))):
    return create_car(request,db)
    

@router.get("/get_all")
def get_all_car(db:Session=Depends(get_db), current_user: dict = Depends(get_current_user)):
    all_details=db.query(CarDetails).all()
    return all_details


@router.get("/search_by")
def search_car(car:str,db:Session=Depends(get_db), current_user: dict = Depends(get_current_user)):
    search_item=db.query(CarDetails).filter(CarDetails.model_name==car).first()
    return search_item
