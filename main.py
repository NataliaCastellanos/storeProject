from models.item import Item

item1 = Item("Leche", "Leche entera", 5000)
item2 = Item("Arroz", "Arroz Diana", 10000)
item3 = Item("Azucar", "Azucar refinada", 2500)

items = [item1, item2, item3]

for item in items:
    print("nombre ", item.get_name())
    print("descripción ", item.description)
    print("precio ", item.get_price())
    print("----")