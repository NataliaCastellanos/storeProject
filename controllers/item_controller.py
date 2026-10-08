from models.item import Item
from models.product import Product
from models.service import Service
class ItemController:

    def __init__(self):
        self.items = []

    def add_item(self, name, description, price):
        item = Item(name, description, price)
        self.items.append(item)

    def add_product(self, name, description, price, stock):
        product = Product(name, description, price, stock)
        self.items.append(product)

    def add_service(self, name, description, price, duration):
        service= Service(name, description, price, duration)
        self.items.append(service)

    def get_items(self):
        return self.items.copy()

    
