from models.employee import Employee
from models.client import Client

class UserController:

    def __init__(self):
        self.users = []

    def add_employee (self, name, lastName, email, password, salary):
        employee = Employee(name, lastName, email, password, salary)
        self.users.append(employee)

    def add_client (self, name, lastName, email, password, loyaltyPoints):
        client = Client(name, lastName, email, password, loyaltyPoints)
        self.users.append(client)

    def get_users (self): 
        return self.users.copy()
    