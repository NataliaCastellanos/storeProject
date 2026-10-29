from models.sale import Sale

class SaleController:

    def __init__(self):
        self.sales = []

    def add_sale(self, sale):
        self.sales.append(sale)

    def add_item(self, sale, item, quantity):
        sale.add_item(item, quantity)

    def add_user(self, user, sale):
        sale.set_user(user)

    def get_sales(self):
        return self.sales.copy()
