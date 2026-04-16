from models.item import Item

class Service(Item):

    #Constructor for the Service class
    def __init__(self, new_name, new_price, new_description, new_duration):
        super().__init__(new_name, new_price, new_description)
        self.set_duration(new_duration)

    # Getter for the service duration    
    def get_duration(self):
        return self._duration    
    
    # Setter for the service duration
    def set_duration(self, new_duration):
        if(new_duration > 0):
            self._duration = new_duration
        else:
            print("The duration must be greater than 0")