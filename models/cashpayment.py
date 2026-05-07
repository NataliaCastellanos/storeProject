from models.paymentmethod import PaymentMethod

class CashPayment(PaymentMethod):

    # Constructor
    def __init__(self, new_amount, new_cash_received):
        super().__init__(new_amount)
        self.set_cash_received(new_cash_received)
        
    # Getter for cash received
    def get_cash_received(self):
        return self._cash_received

    # Setter for cash received
    def set_cash_received(self, new_cash_received):
        if(new_cash_received > 0):
            self._cash_received = new_cash_received
        else:
            print("The cash received can not be negative")

    #Process payment method
    def process_payment(self, new_approved):
        change = self.get_cash_received() - self.get_amount()

        if change < 0:
            return "The cash received is not enough to complete the payment"
        
        return (f"Cash payment approved. Change: {change}")
    



