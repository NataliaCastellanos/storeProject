from models.item import Item

class ItemController:

    def __init__(self):
        self.items = []

    def add_item(self, name, description, price):
        item = Item(name, description, price)
        self.items.append(item)

    def get_items(self):
        return self.items.copy()

    
