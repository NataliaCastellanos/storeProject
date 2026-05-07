from models.paymentmethod import PaymentMethod

class TransferPayment(PaymentMethod):

    # Constructor
    def __init__(self, new_amount, new_reference_code):
        super().__init__(new_amount)
        self.set_reference_code(new_reference_code)

    # Getter for reference_code
    def get_reference_code(self):
        return self._reference_code
    
    # Setter for reference codde
    def set_reference_code(self, new_reference_code):
        if(new_reference_code != ""):
            self._reference_code = new_reference_code
        else: 
            print("The reference code can not be empty")
    
    # Process tranfer payment
    def process_payment(self, new_approved):
        if(new_approved == True):
            return (f"Tranfer payment approved with reference: {self.get_reference_code()}")
        else:
            return ("Tranfer payment rejected")