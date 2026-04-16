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