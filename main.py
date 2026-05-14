from models.product import Product
from models.service import Service
from models.client import Client
from models.employee import Employee
from models.cashpayment import CashPayment
from models.cardpayment import CardPayment
from models.transferpayment import TransferPayment
from models.sale import Sale

catalog = []
users = []
sales = []

def show_menu():
    print("\n STORE")
    print("1. Add product")
    print("2. Add service")
    print("3. Add client")
    print("4. Add employee")
    print("5. Show catalog")
    print("6. Show users")
    print("7. Create sale")
    print("8. Exit")

def add_product():
    print("\nAdd product")

    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    description = input("Enter product description: ")
    stock = int(input("Enter product stock: "))

    product = Product(name, price, description, stock)
    catalog.append(product)
    print("Product added successfully")

def add_service():
    print("\n Add service")

    name = input("Enter service name: ")
    price = float(input("Enter service price: "))
    description = input("Enter service description: ")
    duration = int(input("Enter service duration: "))

    service = Service(name, price, description, duration)
    catalog.append(service)
    print("Service added successfully")

def add_client():
    print("\n Add client")

    name = input("Enter client name: ")
    last_name = input("Enter client last name: ")
    email = input("Enter client email: ")
    password = input("Enter client password: ")
    loyalty_points = int(input("Enter client loyalty points: "))

    client = Client(name, last_name, email, password, loyalty_points)
    users.append(client)
    print("Client added successffully")

def add_employee():
    print("\n Add employee")

    name = input("Enter employee name: ")
    last_name = input("Enter employee last name: ")
    email = input("Enter employee email: ")
    password = input("Enter employee password: ")
    salary = float(input("Enter employee salary: "))

    employee = Employee(name, last_name, email, password, salary)
    users.append(employee)
    print("Employee added successfully")

def show_catalog():
    print("\n Catalog")

    for item in catalog:
        print(item.show_info())

def show_users():
    print("\n Users")

    for user in users:
        print(user.show_info())

def create_sale():
    print("\n Create sale")

    client_email = input("Enter client email: ")

    client_found = None

    for user in users:
        if(user.get_email() == client_email and user.get_role() == "Client"):
            client_found = user
            break
    
    if( client_found is None):
        print("Client not found")
        return
    
    sale = Sale(client_found)

    add_item = "yes"

    while(add_item == "yes"):
        item_name = input("Enter item name: ")

        item_found = None

        for item in catalog:
            if(item.get_name() == item_name):
                item_found = item
                break

        if(item_found is None):
            print("Item not found")
            return
        else: 
            sale.add_item(item_found)
            print("Item added successfully")

        add_item = input("Do you want to add another item? (yes/no): ")

    total = sale.calculate_total()

    print(f"\n Sale total: {total}")

    payment = None

    while(payment is None):
        payment_type = input("Enter payment method (cash/card/transfer):")

        if(payment_type == "cash"):
            cash_received = float(input("Enter cash received: "))
            payment = CashPayment(total, cash_received)
        elif(payment_type == "card"):
            card_number = input("Enter card number: ")
            payment = CardPayment(total, card_number)
        elif( payment_type == "transfer"):
            reference_code = input("Enter de reference code: ")
            payment = TransferPayment(total, reference_code)
        else: 
            print("\n Invalid payment method, please try again.")
        
    sale.set_payment_method(payment)
    
    payment_approved = input("\n Was the payment approved? (yes/no): ")
    is_approved = payment_approved == "yes"

    print(payment.process_payment(is_approved))
    
    sales.append(sale)
    print("Sale created successfully")

    sale.show_info()

option = 0

while (option != 8):
    show_menu()

    option = int(input("\n Enter an option (1-8):"))

    if(option == 1):
        add_product()
    elif(option == 2):
        add_service()
    elif(option == 3):
        add_client()
    elif(option == 4):
        add_employee()
    elif(option == 5):
        show_catalog()
    elif(option == 6):
        show_users()
    elif(option == 7):
        create_sale()
    elif(option == 8):
        print("\nClosing system")
    else:
        print("\nInvalid option")

print("Bye")





