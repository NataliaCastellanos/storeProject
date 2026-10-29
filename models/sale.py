
from datetime import date
from models.saleDetail import SaleDetail

class Sale:

    def __init__(self, user = None):
        self.set_user(user)
        self._details = []
        self._saleDate = date.today()

    def get_user(self):
        return self._user

    def set_user(self, user):
        self._user = user

    def get_details(self):
        return self._details

    def get_saleDate(self):
        return self._saleDate

    def add_item(self, item, quantity):
        detail = SaleDetail(item, quantity)
        self._details.append(detail)

    def calculate_total(self):
        total = 0

        for detail in self._details:
            # total = total + detail.calculate_subtotal()
            total +=detail.calculate_subtotal()

        return total

    def show_info(self):
        information = (
            f"Usuario: {self.get_user().name} {self.get_user().lastName}\n"
            f"Fecha: {self.get_saleDate()}\n"
            f"Detalle:\n"
        )

        for detail in self._details:
            information += (
                f"Producto: {detail.item.get_name()} - "
                f"Cantidad:  {detail.get_quantity()} - "
                f"Subtotal:  {detail.calculate_subtotal()}\n"
            )

        information += (
            f"Total: {self.calculate_total()}"
        )

        return information


        
