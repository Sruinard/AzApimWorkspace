from fastapi import FastAPI
from typing import List
from repo import Bookings, Booking
import uvicorn


app = FastAPI()


@app.get('/')
def homepage():
    return "booking application"

@app.get('/bookings')
def get_bookings() -> List[Booking]:
    return Bookings.get_bookings()


@app.get('/bookings/{id}')
def get_booking_by_id(id: int) -> Booking:
    return Bookings.get_bookings_by_id(id)

@app.post('/bookings')
def add_booking(booking: Booking) -> None:
    return Bookings.add_booking(origin=booking.origin, dest=booking.dest)


if __name__ == "__main__":
    uvicorn.run(app, port=8080)