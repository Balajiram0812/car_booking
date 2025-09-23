from sqlalchemy import Column, Integer, String, Float,Boolean,ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class CarDetails(Base):
    __tablename__ = "car_details"

    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String(50), nullable=False)
    manufacture_year = Column(Integer, nullable=False)
    insurance_cover = Column(Integer, nullable=True)
    color = Column(String(50))
    engine = Column(String(50))
    power = Column(String(50))
    torque = Column(String(50))
    variant = Column(String(50))
    price = Column(Integer, nullable=False)
    tax = Column(Float) 

    car_detail=relationship('Booking_Details',back_populates='booking_details')

class register(Base):
    __tablename__="register"

    id=Column(Integer, index=True, primary_key=True)
    first_name=Column(String(50), nullable=False)
    last_name=Column(String(50), nullable=False)
    email=Column(String(50), unique=True)
    password=Column(String(100))
    role=Column(String(50), default= "user")
    genter=Column(String(50))
    age=Column(Integer)



class Booking_Details(Base):
    __tablename__="booking_details"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100), nullable=False)
    booking_date = Column(String(50), nullable=False)
    delivery_date = Column(String(50))
    delivery_details = Column(Boolean, default=False)
    booking_car=Column(Integer,ForeignKey('car_details.id'))

    booking_details = relationship('CarDetails', back_populates='car_detail')


