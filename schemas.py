from pydantic import BaseModel,EmailStr
from typing import Literal

class add_car_details(BaseModel):
    model_name: str
    manufacture_year: int
    insurance_cover: int | None = None
    color: str
    engine: str
    power: str
    torque: str
    variant: str
    price: int
    tax: float

class add_car(add_car_details):
    pass    
    class config:
        orm_mode=True

class register_schemas(BaseModel):
    first_name:str
    last_name:str
    email:EmailStr
    password:str
    re_password:str
    role: Literal["user", "admin", "org"] = "user"
    genter:str
    age:int

class register_responce(BaseModel):
    first_name:str
    last_name:str
    email:str

    class config:
        orm_mode=True

class booking_details_schemas(BaseModel):
    user_name:str
    booking_car:int 
   

class booked_car(booking_details_schemas):
    booking_details:add_car

    class config:
        orm_mode=True


class booked_car_details(booking_details_schemas):
    booking_details: add_car   

    class Config:
        orm_mode = True

        
class login(BaseModel):
     username:str
     password:str
        
        
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
    role:str | None=None

