from fastapi import FastAPI
import uvicorn
from database import Base, engine
from service import car,register,booking,auth

app=FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(car.router)
app.include_router(register.router)
app.include_router(booking.router)

@app.get("/")
def get():
    return "hello"

if __name__=="__main__":
    uvicorn.run("main:app", port=8010)