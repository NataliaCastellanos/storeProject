from models.product import Product
from models.service import Service
from models.client import Client
from models.employee import Employee
from models.cashpayment import CashPayment
from models.cardpayment import CardPeryment
from models.transferpayment import TransferPayment
from models.sale import Sale

productLeche = Product("Leche", 3500, "Leche entera", 10)
productPan = Product("Pan", 1500, "", 8)
productArroz = Product("Arroz", 7500, "Arroz blanco", 9)

serviceLimpieza = Service("Limpieza", 50000, "Servicio de limpieza", 120)
serviceConsultoria = Service("Consultaría", 250000, "Servicio de consultoría", 60)

print(productLeche.show_info())
print(productPan.show_info())
print(productArroz.show_info())

print(serviceLimpieza.show_info())
print(serviceConsultoria.show_info())

catalog = [
    productLeche,
    productPan, 
    productArroz,
    serviceConsultoria,
    serviceLimpieza
]

print("Catalog")
for item in catalog:
    print(item.show_info())
    print(item.calculate_total())

#------------------------------------------------------------------------
clientNatalia= Client("Natalia", "Castellanos", "ncastellanos@umanizales.edu.co", "123456789", 20)
clientMiguel = Client("Miguel", "Toro", "migueltoro@gmail.com", "987654321", 100)
employeeSofia = Employee("Sofia", "Arias", "sofiarias@gmail.com", "741852963", 200000)

users = [
    clientNatalia,
    clientMiguel,
    employeeSofia
]

print("\n Users")
for user in users:
    print(user.show_info())

#userEmail= input("Enter your email: ")
#userPassword = input("Enter your password: ")

#for user in users:
#    print(user.login(userEmail, userPassword))

#-----------------------------------------------------------------------

cashPayment1= CashPayment(14500, 20000)
cashPayment2= CashPayment(14500, 10000)
cardPayment1= CardPeryment(20000, "1234 5678 9101 1121")
cardPayment2= CardPeryment(20000, "1234 5678 9101 1123")
transferPayment1 = TransferPayment(35000, "abc123456")
transferPayment2 = TransferPayment(35000, "abc123489")

print(cashPayment1.process_payment(True))
print(cashPayment2.process_payment(True))
print(cardPayment1.process_payment(True))
print(cardPayment2.process_payment(False))
print(transferPayment1.process_payment(True))
print(transferPayment2.process_payment(False))

print("Sale")
sale = Sale(clientNatalia)

sale.add_item(productLeche)
sale.add_item(productPan)

sale.set_payment_method(cashPayment1)

sale.show_info()
