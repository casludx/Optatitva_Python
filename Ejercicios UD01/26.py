def calcular_salario_bruto(horas, tarifa):
    if horas <= 35:
        salario_bruto = horas * tarifa
    else:
        pago_normal = 35 * tarifa
        horas_extra = horas - 35 
        pago_extra = horas_extra * (tarifa * 1.5)
        salario_bruto = pago_normal + pago_extra
    return salario_bruto

def calcular_impuestos(salario_bruto):
    impuestos_totales = 0
    
    limite_tramo_1 = 500
    limite_tramo_2 = 900
    
    tasa_tramo_2 = 0.25
    tasa_tramo_3 = 0.45
    
    if salario_bruto > limite_tramo_2:
        base_tramo3 = salario_bruto - limite_tramo_2
        impuesto_tramo3 = base_tramo3 * tasa_tramo_3
        
        base_tramo2 = 400
        impuesto_tramo2 = base_tramo2 * tasa_tramo_2
        
        impuestos_totales = impuesto_tramo2 + impuesto_tramo3
        
    elif salario_bruto > limite_tramo_1:
        base_tramo2 = salario_bruto - limite_tramo_1
        impuesto_tramo2 = base_tramo2 * tasa_tramo_2
        
        impuestos_totales = impuesto_tramo2
    
    else:
        impuestos_totales = 0
    
    return impuestos_totales

try:
    nombre = str(input("Introduce el nombre del trabajador: "))
    horas_trabajadas = float(input("Introduce el total de horas trabajadas esta semana: "))
    tarifa_normal = float(input("Introduce la tarifa normal por hora (€): "))
    
    salario_bruto = calcular_salario_bruto(horas_trabajadas, tarifa_normal)
    total_impuestos = calcular_impuestos(salario_bruto)
    salario_neto = salario_bruto - total_impuestos
    
    print("\n" + "="*40)
    print(f"--- 🧾 Resumen de Nómina Semanal ---")
    print(f"Trabajador: \t\t{nombre}")
    print("="*40)
    print(f"Salario Bruto: \t\t{salario_bruto:.2f} €")
    print(f"Tasas (Impuestos): \t{total_impuestos:.2f} €")
    print("-"*40)
    print(f"Salario Neto: \t\t{salario_neto:.2f} €")
    print("="*40)
    
except ValueError:
    print("\nError: Has introducido un valor no númerico en las horas o la tarifa")
except Exception as e:
    print(f"\nHa ocurrido un error inesperado: {e}")
    