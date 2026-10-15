from models.user import User

class Client(User): 

    def __init__(self, name, lastName, email, password, loyaltyPoints):
        super().__init__(name, lastName, email, password)
        self.set_loyaltyPoints(loyaltyPoints)

    def get_loyaltyPoints(self):
        return self._loyaltyPoints

    def set_loyaltyPoints(self, loyaltyPoints):
        if loyaltyPoints > 0:
            self._loyaltyPoints = loyaltyPoints
        else: 
            raise ValueError("Los puntos de fidelización deben ser mayores que cero")

    def show_info(self):
        return f"{super().show_info()} - Puntos: {self.get_loyaltyPoints()}"