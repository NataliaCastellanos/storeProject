class Item:

    # Constructor to initialize the item attributes
    def __init__(self, new_name, new_price, new_description):
        self.set_name(new_name) 
        self.set_price(new_price)
        self.description = new_description

    # Getter for the item name
    def get_name(self):
        return self._name

    # Setter for the item name
    def set_name(self, new_name):
        if(new_name != ""):
            self._name = new_name
        else:
            print("The item name cannot be empty")

    # Getter for the item price
    def get_price(self):
        return self._price
    
    # Setter for the item price
    def set_price(self, new_price):
        if(new_price > 0):
            self._price = new_price
        else:
            print("The price must be greater than 0")