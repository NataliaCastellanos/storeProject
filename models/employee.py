from models.user import User

class Employee(User): 
    # Constructor for the Employee class
    def __init__(self, new_name, new_last_name, new_email, new_password, new_salary):
        super().__init__(new_name, new_last_name, new_email, new_password)
        self.set_salary(new_salary)

    # Getter for the employee salary
    def get_salary(self):
        return self._salary
    
    # Setter for the employee salary
    def set_salary(self, new_salary):
        if(new_salary > 0):
            self._salary = new_salary
        else:
            print("The salary must be greater than 0")

    # Show_info
    def show_info(self):
        return(f"Name: {self.get_name()} {self.get_last_name()} \n"
               f"Email: {self.get_email()} \n"
               f"Salary: {self.get_salary()}")
    
    # Get role
    def get_role(self):
        return "Employee"
    
    # Login
    def login(self, email, password):
        if( self.get_email() == email and self.get_password() == password):
            return (f"{self.get_role()} bienvenido")
        else:
            return ("Invalid credetials for this employee")
        
    