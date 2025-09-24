from fastapi import APIRouter,Depends,HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from dto.schemas import booking_details_schemas,booked_car,booked_car_details
from datetime import datetime
from model.model import Booking_Details,CarDetails
from repo.boooking import booking_details_repo,get_by_id_car, update_booking_details

router=APIRouter(
    tags=["booking details"]
)

@router.post("/booking_details",  response_model=booked_car)
def booking_details(request:booking_details_schemas, db: Session=Depends(get_db)):
    return booking_details_repo(request,db)


@router.get("/booking/{userid}/details", response_model=booked_car_details)
def get_by_id(userid: int, db: Session = Depends(get_db)):
    return get_by_id_car(userid, db)


@router.put("/update/{userid}/details", response_model=booked_car)
def update_details(userid: int, change_car: int, db: Session = Depends(get_db)):
    return update_booking_details(userid, change_car, db)