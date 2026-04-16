from models.product import Product
from models.service import Service
from models.client import Client
from models.employee import Employee

# Create a product instance
product1 = Product("Leche", 3500, "Leche entera de vaca", 100)

print("Producto 1")
print(f"Producto: {product1.get_name()}")
print(f"Precio: {product1.get_price()}")
print(f"Descripción: {product1.description}")
print(f"Stock disponible: {product1.get_stock()} \n")

# Create another product instance
product2 = Product("Pan", 1500, "Pan integral de caja", 50)
print("Producto 2")
print(f"Producto: {product2.get_name()}")
print(f"Precio: {product2.get_price()}")
print(f"Descripción: {product2.description}")
print(f"Stock disponible: {product2.get_stock()}")

# Create a third product instance
product3 = Product("Huevos", 5000, "Huevos de gallina, docena", 200)
print("\nProducto 3")
print(f"Producto: {product3.get_name()}")
print(f"Precio: {product3.get_price()}")
print(f"Descripción: {product3.description}")
print(f"Stock disponible: {product3.get_stock()}")

# Create a fourth product instance with an empty description
product4 = Product("Arroz", 5000, "", 80)
print("\nProducto 4")
print(f"Producto: {product4.get_name()}")
print(f"Precio: {product4.get_price()}")
print(f"Descripción: {product4.description}")
print(f"Stock disponible: {product4.get_stock()}")

# Service instances
service1 = Service("Maintenance", 20000, "General maintenance service", 30)
print("\nServicio 1")
print(f"Servicio: {service1.get_name()}")
print(f"Precio: {service1.get_price()}")
print(f"Descripción: {service1.description}")
print(f"Duración: {service1.get_duration()}")

service2 = Service("Cleaning", 15000, "Professional cleaning service", 20)
print("\nServicio 2")
print(f"Servicio: {service2.get_name()}")
print(f"Precio: {service2.get_price()}")
print(f"Descripción: {service2.description}")
print(f"Duración: {service2.get_duration()}")

service3 = Service("Consulting", 50000, "Business consulting service", 60)
print("\nServicio 3")
print(f"Servicio: {service3.get_name()}")
print(f"Precio: {service3.get_price()}")
print(f"Descripción: {service3.description}")
print(f"Duración: {service3.get_duration()}")

#------------------------------------------------------------

# Client instances
client1 = Client("John", "Doe", "john.doe@example.com", "password123", 0) 
print("\nCliente 1")
print(f"Nombre: {client1.get_name()} {client1.get_last_name()}")
print(f"Email: {client1.get_email()}")
print(f"Puntos de lealtad: {client1.get_loyalty_points()}")