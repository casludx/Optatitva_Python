#Dibuja un ordinograma que dado el precio de un artículo y el precio de venta real nos
#muestre el porcentaje de descuento realizado.

precio = int(input("Dime el precio real del producto"))
precioDescuento = int(input("Dime el precio del producto con el descuento"))

descuento = precio - precioDescuento
porcentaje = (descuento / precio) * 100

print(f"El porcentaje del descuento realizado es: {porcentaje}")
