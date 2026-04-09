from models.product import Product

# Create a product instance
product1 = Product("Leche", 3500, "Leche entera de vaca", 100)
print("Producto 1")
print(f"Producto: {product1.name}")
print(f"Precio: {product1.price}")
print(f"Descripción: {product1.description}")
print(f"Stock disponible: {product1.stock} \n")

# Create another product instance
product2 = Product("Pan", 1500, "Pan integral de caja", 50)

print("Producto 2")
print(f"Producto: {product2.name}")
print(f"Precio: {product2.price}")
print(f"Descripción: {product2.description}")
print(f"Stock disponible: {product2.stock}")

# Create a third product instance
product3 = Product("Huevos", 5000, "Huevos de gallina, docena", 200)
print("\nProducto 3")
print(f"Producto: {product3.name}")
print(f"Precio: {product3.price}")
print(f"Descripción: {product3.description}")
print(f"Stock disponible: {product3.stock}")