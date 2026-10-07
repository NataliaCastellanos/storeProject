class Item:

    def __init__(self, name, description, price):
        # self.name = name
        self.set_name(name)
        self.description = description
        #self.price = price
        self.set_price(price)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if(name != ""): 
            self._name = name
        else: 
            raise ValueError("El nombre no puede ser vacío")
        
    def get_price(self):
        return self._price

    def set_price(self, price):
        if(price > 0):
            self._price = price
        else: 
            raise ValueError("El precio del producto no puede ser 0 o negativo")
        
        