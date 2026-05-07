from models.user import User
class Employee(User):

    def __init__(self, new_name, new_last_name, new_email, new_password, new_salary):
        super().__init__(new_name, new_last_name, new_email, new_password)
        self.set_salary(new_salary)

    # Getter for salary
    def get_salary(self):
        return self._salary
    
    #Setter for salary
    def set_salary(self, new_salary):
        if(new_salary > 0):
            self._salary = new_salary
        else: 
            print("The salary must be greate than 0")

    #Get role
    def get_role(self):
        return ("Employee")
    
    #Show_info
    def show_info(self):
        return (f"Name: {self.get_name()}, Last Name: {self.get_last_name()}, Email: {self.get_email()}, Role: {self.get_role()}, Salary: {self.get_salary()}")
        
    # Login
    def login(self, email, password):
        if(self._email == email and self._password == password):
            return (f"Welcome, {self.get_role()} {self.get_name()}. You can access to users module")
        else:
            return (f"Invalid credentials for {self.get_role()}")
    