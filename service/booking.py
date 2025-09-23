from fastapi import APIRouter,Depends,HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas import booking_details_schemas,booked_car,booked_car_details
from datetime import datetime
from model import Booking_Details,CarDetails



router=APIRouter(
    tags=["booking details"]
)


@router.post("/booking_details",  response_model=booked_car)
def booking_details(request:booking_details_schemas, db: Session=Depends(get_db)):

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


@router.get("/booking/{userid}/details", response_model=booked_car_details)
def get_by_id(userid: int, db: Session = Depends(get_db)):
    booking = db.query(Booking_Details).filter(Booking_Details.id == userid).first()

    if not booking:
        raise HTTPException(status_code=404, detail=f"data not found {userid}")

    return booking


@router.put("/update/{userid}/details", response_model=booked_car)
def update_details(userid: int, change_car: int, db: Session = Depends(get_db)):
    update = db.query(Booking_Details).filter(Booking_Details.id == userid).first()

    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Data not found for id {userid}")
    
    update.booking_car = change_car  
    db.commit()
    db.refresh(update)

    return update