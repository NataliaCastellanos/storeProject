from models.item import Item

class Service(Item):

    # Constructor
    def __init__(self, new_name, new_price, new_description, new_duration):
        super().__init__(new_name, new_price, new_description)
        self.set_duration(new_duration)

    # Getter for duration
    def get_duration(self):
        return self._duration
    
    # Setter for duration
    def set_duration(self, new_duration):
        if(new_duration > 0):
            self._duration = new_duration
        else: 
            print("The duration can not be negative")

    # Show info
    def show_info(self):
        return (f"Service: {self.get_name()}, price: {self.get_price()}, description: {self.description}, duration: {self.get_duration()}")
    
     # Calculate total
    def calculate_total(self):
        return self.get_price() * self.get_duration()