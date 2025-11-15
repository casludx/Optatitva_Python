"""
Una farmacia desea un programa para ingresar el valor de compra y calcular lo siguiente: si
el pago se efectúa al “contado”, calcular un descuento del 5%; pero si el pago es con “tarjeta”
se incrementa un recargo del 3% al valor de compra. Calcular y visualizar el descuento o recargo
según sea el caso y el total a pagar de la compra
"""

pago = int(input("Introduce la cantidad a pagar: "))
manera = str(input("Pagará usted al contado o con tarjeta: ")).lower().strip()
pago_final = 0

if manera == "contado":
    descuento = 0.05 * pago
    pago_final = pago - descuento
    print("\nSe le ha aplicado un descuento del 5%")
    print(f"Su pago total al pagar al contado es de:{pago_final}")

elif manera == "tarjeta":
    descuento = 0.03 * pago
    pago_final = pago + descuento
    print("\nSe le ha aplicado un recargo del 3%")
    print(f"Su pago total al pagar con tarjeta es de: {pago_final}")

else:
    print("\nHa introducido usted una manera de pago diferente")