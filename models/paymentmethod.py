from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    # Constructor
    def __init__(self, new_amount):
        self.set_amount(new_amount)

    # Getter for amount
    def get_amount(self):
        return self._amount
    
    # Setter for amount
    def set_amount(self, new_amount):
        if(new_amount >= 0):
            self._amount = new_amount
        else: 
            print("The amount can not be negative")

    # process_payment
    @abstractmethod
    def process_payment(self, new_approved):
        pass