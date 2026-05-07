from models.user import User
from models.item import Item
from models.paymentmethod import PaymentMethod

class Sale:

    # Constructor
    def __init__(self, user):
        self._user = user
        self._items = []
        self._payment_method = None
    
    # Add an item into items
    def add_item(self, item):
        self._items.append(item)
    
    # Assign the payment method
    def set_payment_method(self, payment_method):
        self._payment_method = payment_method

    # Calculate total's sale
    def calculate_total(self):

        total = 0

        for item in self._items:
            total = total + item.get_price()

        return total
    
    def show_info(self):
        print(f"User: {self._user.get_name()} {self._user.get_last_name()}")

        print("\n Items: ")

        for item in self._items:
            print(item.show_info())
        
        print(f"Total: {self.calculate_total()}")

        if(self._payment_method is None):
            print("Payment method can not be empty")
        else: 
            print(f"Payment Method: \n {self._payment_method.process_payment(True)}")