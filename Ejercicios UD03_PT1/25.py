"""
La universidad ha categorizado las matrículas de acuerdo a la facultad que va a estudiar el
postulante. Ingrese por teclado el nombre del postulante y la facultad que va a estudiar, muestre
el importe, la mensualidad, el IGV 18% (importe + mensualidad) y el monto final a pagar. 
"""

nombre = str(input("Introduce su nombre: "))
facultad = str(input("Introduce la facultad en la que va a estudiar sin abreviaciones: ")).lower().strip()

igv = 0
total_pagar = 0

if facultad == "ingenieria de sistemas":
    importe = 350
    mensualidad = 650
    print(f"\nUsted, {nombre} tendrá que pagar: ")
    print(f"\n{importe}€ de importe y {mensualidad}€ de mensualidad")
    igv = (importe + mensualidad) * 0.18
    print(f"\n{igv}€ de IGV")
    total_pagar = importe + mensualidad + igv
    print(f"\n{total_pagar}€ será el total que deba abonar")

elif facultad == "derecho":
    importe = 300
    mensualidad = 550
    print(f"\nUsted, {nombre} tendrá que pagar: ")
    print(f"\n{importe}€ de importe y {mensualidad}€ de mensualidad")
    igv = (importe + mensualidad) * 0.18
    print(f"\n{igv}€ de IGV")
    total_pagar = importe + mensualidad + igv
    print(f"\n{total_pagar}€ será el total que deba abonar")

elif facultad == "ingenieria naviera":
    importe = 300
    mensualidad = 500
    print(f"\nUsted, {nombre} tendrá que pagar: ")
    print(f"\n{importe}€ de importe y {mensualidad}€ de mensualidad")
    igv = (importe + mensualidad) * 0.18
    print(f"\n{igv}€ de IGV")
    total_pagar = importe + mensualidad + igv
    print(f"\n{total_pagar}€ será el total que deba abonar")
    
elif facultad == "ingenieria pesquera":
    importe = 310
    mensualidad = 460
    print(f"\nUsted, {nombre} tendrá que pagar: ")
    print(f"\n{importe}€ de importe y {mensualidad}€ de mensualidad")
    igv = (importe + mensualidad) * 0.18
    print(f"\n{igv}€ de IGV")
    total_pagar = importe + mensualidad + igv
    print(f"\n{total_pagar}€ será el total que deba abonar")
    
elif facultad == "contabilidad":
    importe = 280
    mensualidad = 490
    print(f"\nUsted, {nombre} tendrá que pagar: ")
    print(f"\n{importe}€ de importe y {mensualidad}€ de mensualidad")
    igv = (importe + mensualidad) * 0.18
    print(f"\n{igv}€ de IGV")
    total_pagar = importe + mensualidad + igv
    print(f"\n{total_pagar}€ será el total que deba abonar")
    
elif facultad == "administracion":
    importe = 360
    mensualidad = 520
    print(f"\nUsted, {nombre} tendrá que pagar: ")
    print(f"\n{importe}€ de importe y {mensualidad}€ de mensualidad")
    igv = (importe + mensualidad) * 0.18
    print(f"\n{igv}€ de IGV")
    total_pagar = importe + mensualidad + igv
    print(f"\n{total_pagar}€ será el total que deba abonar")
    
else:
    print("Debe introducir algunas de las facultades de nuestra universidad")