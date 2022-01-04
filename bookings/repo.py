from typing import Optional
from pydantic import BaseModel

class Booking(BaseModel):

    origin: str
    dest: str
    id: Optional[int]


class BookingsRepo():

    def __init__(self):
        self.counter = 0
        self.bookings = []
        for origin, dest in [('Ams', 'Sydney'), ('Melbourne', 'London')]:
            self.add_booking(origin=origin, dest=dest)

    def get_bookings(self):
        return self.bookings

    def get_bookings_by_id(self, id):
        return [booking for booking in self.bookings if booking.id == id][0]

    def add_booking(self, origin, dest):
        booking = Booking(id=self.counter, origin=origin, dest=dest)
        self.counter += 1
        self.bookings.append(booking)
        return booking

Bookings = BookingsRepo()