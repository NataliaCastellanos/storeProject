class SaleDetail:

    def __init__(self, item, quantity):
        self.item = item 
        self.set_quantity(quantity)

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, quantity):
        if quantity > 0:
            self._quantity = quantity
        else:
            raise ValueError("La cantidad comprada debe ser mayor que cero")

    def calculate_subtotal(self):
        return self.item.get_price() * self.get_quantity()