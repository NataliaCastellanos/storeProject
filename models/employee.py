from models.user import User

class Employee(User):

    def __init__(self, name, lastName, email, password, salary):
        super().__init__(name, lastName, email, password)
        self.set_salary(salary)

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        if salary > 0:
            self._salary = salary
        else:
            raise ValueError("El salario debe ser un valor mayor que cero")

    def show_info(self):
        return f"{super().show_info()} - Salario: {self.get_salary()}"