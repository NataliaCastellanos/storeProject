from models.user import User
class Client(User):

    def __init__(self, new_name, new_last_name, new_email, new_password, new_loyalty_points ):
        super().__init__(new_name, new_last_name, new_email, new_password)
        self.set_loyalty_points(new_loyalty_points)

    #Getter for loyalty points
    def get_loyalty_points(self):
        return self._loyalty_points
    
    #Setter for loyalty points
    def set_loyalty_points(self, new_loyalty_points):
        if(new_loyalty_points >= 0):
            self._loyalty_points = new_loyalty_points
        else:
            print("The Loyalty Points can not be negative")
    
    #Get role
    def get_role(self):
        return ("Client")
    
    #Show_info
    def show_info(self):
        return (f"Name: {self.get_name()}, Last Name: {self.get_last_name()}, Email: {self.get_email()}, Role: {self.get_role()}, Loyalty Points: {self.get_loyalty_points()}")
        
    # Login
    def login(self, email, password):
        if(self._email == email and self._password == password):
            return (f"Welcome, {self.get_role()} {self.get_name()}. You can see the product's list")
        else:
            return (f"Invalid credentials for {self.get_role()}")