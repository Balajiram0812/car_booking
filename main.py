from fastapi import FastAPI
import uvicorn
from controller import auth_controller, booking_controller, car_controller
from database import Base, engine
from controller import register_controller
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from sqlalchemy.exc import IntegrityError
from excaption import (http_exception_handler,validation_exception_handler,sqlalchemy_exception_handler,global_exception_handler)

app=FastAPI()
Base.metadata.create_all(bind=engine)

app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(IntegrityError, sqlalchemy_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)

app.include_router(auth_controller.router)
app.include_router(car_controller.router)
app.include_router(register_controller.router)
app.include_router(booking_controller.router)

@app.get("/")
def get():
    return "hello"

if __name__=="__main__":
    uvicorn.run("main:app", port=8010)