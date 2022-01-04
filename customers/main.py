from fastapi import FastAPI
from typing import List
from repo import Customers, Customer
import uvicorn


app = FastAPI()


@app.get('/')
def homepage():
    return "customer application"

@app.get('/customer')
def get_customer() -> List[Customer]:
    return Customers.get_customers()


@app.get('/customer/{id}')
def get_customer_by_id(id: int) -> Customer:
    return Customers.get_customer_by_id(id)

@app.post('/customer')
def add_customer(customer: Customer) -> Customer:
    return Customers.add_customer(name=customer.name)


if __name__ == "__main__":
    uvicorn.run(app, port=8080)