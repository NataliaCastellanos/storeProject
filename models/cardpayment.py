from models.paymentmethod import PaymentMethod

class CardPeryment(PaymentMethod):

    # Constructor
    def __init__(self, new_amount, new_card_number):
        super().__init__(new_amount)
        self.set_card_number(new_card_number)

    # Getter for card number
    def get_card_number(self):
        return self._card_number

    # Setter for card number
    def set_card_number(self, new_card_number):
        if( new_card_number != ""):
            self._card_number = new_card_number
        else: 
            print("The card number can not be empty")
    
    #Process card paymente 
    def process_payment(self, new_approved):
        if(new_approved == True):
            return (f"Payment approved")
        else: 
            return (f"Payment rejected")