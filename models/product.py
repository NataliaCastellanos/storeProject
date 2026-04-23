from models.item import Item
class Product(Item):
    
    # Constructor to initialize the product attributes
    def __init__(self, new_name, new_price, new_description, new_stock):
        super().__init__(new_name, new_price, new_description)
        self.set_stock(new_stock)

    # Getter for the product stock
    def get_stock(self):
        return self._stock
    
    # Setter for the product stock
    def set_stock(self, new_stock):
        if(new_stock >= 0):
            self._stock = new_stock
        else:
            print("The stock cannot be negative")

    # Describe method
    def describe(self):
        return (f"Product: {self.get_name()}, price: {self.get_price()}, stock: {self.get_stock()}")
    
    # Calculte total
    def calculate_total(self):
        return self.get_price() * self.get_stock()