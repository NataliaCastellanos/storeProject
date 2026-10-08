from models.item import Item

class Service(Item):

    def __init__(self, name, description, price, duration):
        super().__init__(name, description, price)
        self.set_duration(duration)

    def get_duration(self):
        return self._duration

    def set_duration(self, duration):
        if(duration > 0):
            self._duration = duration
        else: 
            raise ValueError("La duración del servicio no puede ser 0 o menor a 0")

    def show_info(self):
        return f"{super().show_info()} - Duración del servicio: {self.get_duration()}"