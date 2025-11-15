#Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares,

saldo_inicial = 1000

print("-----Bienvenido al cajero virtual-----")

while True:
    print(f"\nSu saldo actual es de {saldo_inicial}")
    print("\nMenú de opciones")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Salir")
    
    opcion = int(input("Selecciona una de las tres opciones (1, 2 o 3): "))
    
    if opcion == 1:
        print("\n---Ingresar dinero---")
        
        ingreso = float(input("¿Cuanto dinero desea ingresar:? "))
        
        if ingreso > 0:
            saldo_inicial += ingreso
            print(f"Su ingreso ha sido exitoso, su saldo inicial se ha convertido en {saldo_inicial}")
        else:
            print("Debe ingresar una cantidad positiva")
    
    elif opcion == 2:
        print("\n---Retirar dinero---")
        
        retirada = float(input("¿Cuanto dinero desea retirar:? "))
        
        if retirada <= 0:
            print("La cantidad debe ser positiva")
        elif retirada > saldo_inicial:
            print(f"\nNo tiene fondo suficientes. Su saldo es de {saldo_inicial}")
        else:
            saldo_inicial -= retirada
            print(f"Su retirada ha sido exitosa, su saldo inicial se ha convertido en {saldo_inicial}")
    
    elif opcion == 3:
        print("Gracias por usar el cajero virtual, hasta la proxima")
        break
    
    else:
        print("\nOpción no valida, introduzca 1, 2 o 3")