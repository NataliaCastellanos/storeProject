from models.item import Item

class Product(Item):

    def __init__(self, name, description, price, stock):
        super().__init__(name, description, price)
        self.set_stock(stock)

    def get_stock(self):
        return self._stock

    def set_stock(self, stock):
        if(stock >= 0):
            self._stock = stock
        else:
            raise ValueError("Las existencias deber ser un número entero positivo")

    def show_info(self):
        return f"{super().show_info()} - Existencias:  {self.get_stock()}"