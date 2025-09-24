from model.model import CarDetails,Booking_Details
from fastapi import HTTPException
from sqlalchemy.orm import Session
from dto.schemas import booking_details_schemas
from datetime import datetime

def booking_details_repo(request:booking_details_schemas,db:Session):
    car = db.query(CarDetails).filter(CarDetails.id == request.booking_car).first()
    if not car:
        raise HTTPException(status_code=400, detail="Car not found")
    add_booking = Booking_Details(
        user_name=request.user_name,
        booking_date=datetime.utcnow(),
        booking_car=request.booking_car
    )
    db.add(add_booking)
    db.commit()
    db.refresh(add_booking)  
    return add_booking

def get_by_id_car(userid:int,db:Session):
    booking = db.query(Booking_Details).filter(Booking_Details.id == userid).first()
    
    if not booking:
        raise HTTPException(status_code=404, detail=f"data not found {userid}")

    return booking


def update_booking_details(userid:int,change_car:int,db:Session):
    update = db.query(Booking_Details).filter(Booking_Details.id == userid).first()

    if not update:
        raise HTTPException(status_code=404, detail=f"Data not found for id {userid}")
    
    update.booking_car = change_car  
    db.commit()
    db.refresh(update)

    return update
   