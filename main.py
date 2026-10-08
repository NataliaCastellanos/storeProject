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

##--------------------------------------------------------
## main es la función principal
def main():
    item_controller = ItemController()

    while True:
        print("\n Opciones")
        print("1. Agregar artículos")
        print("2. Mostrar artículos")
        print("3. Salir")

        option = input("Selecciona una opción: ")

        match option:
            case "1":
                name = input("Ingresa el nombre del item: ")
                description = input("Ingresa la descripción del item: ")
                price = int(input("Ingresa el precio del item: "))

                item_controller.add_item(name, description, price)
                print("Item agregado con éxito")

            case "2":
                show_items(item_controller)
                
            case "3":
                print("Vuelve pronto")
                break

            case _:
                print("Opción inválida")

if __name__ == "__main__":
    main()

        