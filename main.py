## Esto es un ejemplo de instaciar objetos tipo item
# from models.item import Item

# item1 = Item("Leche", "Leche entera", 5000)
# item2 = Item("Arroz", "Arroz Diana", 10000)
# item3 = Item("Azucar", "Azucar refinada", 2500)

# items = [item1, item2, item3]

# for item in items:
#     print("nombre ", item.get_name())
#     print("descripción ", item.description)
#     print("precio ", item.get_price())
#     print("----")

## --------------------------------------------------------

from controllers.item_controller import ItemController
from controllers.user_controller import UserController
from controllers.sale_controller import SaleController
from models.sale import Sale
## show items crea una copia del array original, 
# verifica que tenga elementos y 
# muestra la información de cada uno

def show_items(item_controller):
    items = item_controller.get_items()

    if not items:
        print("No existen items registrados")
        return 

    for item in items:
        print(item.show_info())    

# show users crea una copia del array original
# verifica existencias de usuarios
# recorre la lista y muestra la información de cada uno
def show_users(user_controller):
    users = user_controller.get_users()

    if not users:
        print("No existen usuarios registrados")
        return

    for user in users:
        print(user.show_info())

#Método para agregar artículos.
def add_items(item_controller, sale_controller, sale):

    items = item_controller.get_items()
    
    if not items:
        print("No existen artículos registrados")
        return

    for item in items:
        print(item.show_info())

    selected_item = input("Ingresa el nombre del artículo")

    for item in items:
        if item.get_name() == selected_item:
            quantity = int(input("Indica la cantidad: "))
            sale_controller.add_item(sale, item, quantity)
            print("Artículo agregado")
            return

    print("Artículo no encontrado")

## Método para agregar usuario
def add_user(user_controller, sale_controller, sale):
    users = user_controller.get_users()
    
    if not users:
        print("No existen usuarios registrados")
        return

    for user in users:
        print(user.show_info())

    selected_user = input("Ingresa el email del usuario")

    for user in users:
        if user.get_email() == selected_user:
            sale_controller.add_user(user, sale)
            print("Usuario agregado")
            return
        
    print("Usuario no encontrado")

def sale_menu(item_controller, user_controller, sale_controller): 
    sale = Sale()

    while True:
        print("\n Nueva venta")
        print("1. Agregar artículo")
        print("2. Agregar usuario")
        print("3. Mostrar venta")
        print("4. Salir")

        option = input("Selecciona una opción: ")

        match option:
            case "1": 
               add_items(item_controller, sale_controller, sale)

            case "2":
                add_user(user_controller, sale_controller, sale)

            case "3":
                if not sale.get_details():
                    print("Debes agregar al menos un artículo")
                    continue

                if sale.get_user() is None:
                    print("Debes agregar un usuario")

                sale_controller.add_sale(sale)
                print ("Venta registrada")
                print (sale.show_info())
                return 

            case "4":
                print("Venta cancelada")
                return        

##--------------------------------------------------------
## main es la función principal, contiene el menú y las acciones correspondientes a cada opción
def main():
    item_controller = ItemController()
    user_controller = UserController()
    sale_controller = SaleController()

    while True:
        print("\n Opciones")
        print("1. Agregar producto")
        print("2. Agregar servicio")
        print("3. Mostrar artículos")
        print("4. Agregar empleado")
        print("5. Agregar cliente")
        print("6. Mostrar usuarios")
        print("7. Registrar venta")
        print("8. Salir")

        option = input("Selecciona una opción: ")

        match option:
            case "1":
                name = input("Ingresa el nombre del item: ")
                description = input("Ingresa la descripción del item: ")
                price = float(input("Ingresa el precio del item: "))
                stock = int(input("Ingresa el número de existencias: "))

                item_controller.add_product(name, description, price, stock)
                print("Producto agregado con éxito")

            case "2":
                name = input("Ingresa el nombre del item: ")
                description = input("Ingresa la descripción del item: ")
                price = float(input("Ingresa el precio del item: "))
                duration = int (input("Ingresa la duración del servicio en minutos"))

                item_controller.add_service(name, description, price, duration)
                print("Servicio agregado con éxito")

            case "3":
                show_items(item_controller)

            case "4":
                name = input("Ingresa el nombre del empleado: ")
                lastName = input("Ingresa el apellido del empleado: ")
                email = input("Ingresa el email del empleado: ")
                password = input("Ingresa el password: ")
                salary = float(input("Ingresa el salario asignado: "))

                user_controller.add_employee(name, lastName, email, password, salary)
                print("Empleado agregado con éxito.")

            case "5":
                name = input("Ingresa el nombre del cliente: ")
                lastName = input("Ingresa el apellido del cliente: ")
                email = input("Ingresa el email del cliente: ")
                password = input("Ingresa el password: ")
                loyaltyPoints = int(input("Ingresa los puntos acumulados: "))

                user_controller.add_client(name, lastName, email, password, loyaltyPoints)
                print("Cliente agregado con éxito.")

            case "6": 
                show_users(user_controller)

            case "7": 
                sale_menu(item_controller, user_controller, sale_controller)

            case "8":
                print("Vuelve pronto")
                break

            case _:
                print("Opción inválida")

if __name__ == "__main__":
    main()

        