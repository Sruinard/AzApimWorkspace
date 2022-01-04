from typing import Optional
from pydantic import BaseModel

class Customer(BaseModel):

    name: str
    id: Optional[int]


class CustomerRepo():

    def __init__(self):
        self.counter = 0
        self.customers = []
        for name in ['Stef', 'Jason', 'Lisa']:
            self.add_customer(name=name)

    def get_customers(self):
        return self.customers

    def get_customer_by_id(self, id):
        return [customer for customer in self.customers if customer.id == id][0]

    def add_customer(self, name):
        customer = Customer(id=self.counter, name=name)
        self.counter += 1
        self.customers.append(customer)
        return customer

Customers = CustomerRepo()