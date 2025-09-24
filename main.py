from fastapi import FastAPI
import uvicorn
from controller import auth_controller, booking_controller, car_controller
from database import Base, engine
from controller import register_controller

app=FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(auth_controller.router)
app.include_router(car_controller.router)
app.include_router(register_controller.router)
app.include_router(booking_controller.router)

@app.get("/")
def get():
    return "hello"

if __name__=="__main__":
    uvicorn.run("main:app", port=8010)