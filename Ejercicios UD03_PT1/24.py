"""
Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el día
de la semana; si el día es martes o jueves, se realizará un descuento del 15% por la compra.
Visualizar el descuento y el total a pagar por la compra.
"""

compra = int(input("Introduce el precio total a pagar: "))
dia = str(input("Introduce el día de la semana: ")).lower().strip()
compra_final = 0

if dia == "martes" or dia == "jueves":
    print("Al ser los días especiales tiene usted un descuento del 15%")
    descuento = 0.15 * compra
    print(f"\nEl descuento a realizar es de {descuento}")
    compra_final = compra - descuento
    print(f"\nEl pago total es de: {compra_final}")
else:
    print("Al no estar en los días especiales no se le aplicará descuento")
    print(f"\nSu importe a pagar es de {compra}")