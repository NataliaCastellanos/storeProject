from models.user import User

class Client(User): 
    # Constructor for the Client class
    def __init__(self, new_name, new_last_name, new_email, new_password, new_loyalty_points):
        super().__init__(new_name, new_last_name, new_email, new_password)
        self.set_loyalty_points(new_loyalty_points)

    # Getter for the client loyalty points
    def get_loyalty_points(self):
        return self._loyalty_points
    
    # Setter for the client loyalty points
    def set_loyalty_points(self, new_loyalty_points):
        if(new_loyalty_points >= 0):
            self._loyalty_points = new_loyalty_points
        else:
            print("The loyalty points cannot be negative")
    
    # Show_info
    def show_info(self):
        return(f"Name: {self.get_name()} {self.get_last_name()} \n"
               f"Email: {self.get_email()} \n"
               f"Loyalty points: {self.get_loyalty_points()}")
    
    # Get role
    def get_role(self):
        return "Client"
    
    # Login
    def login(self, email, password):
        if( self.get_email() == email and self.get_password() == password):
            return (f"{self.get_role()} bienvenido")
        else:
            return ("Invalid credetials for this client")