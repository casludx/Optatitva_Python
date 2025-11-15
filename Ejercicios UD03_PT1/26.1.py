import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)

print(f"Los dados que te han tocado son:[{dado1}, {dado2}, {dado3}]")

contador_seis = 0

if dado1 == 6:
    contador_seis += 1
    
if dado2 == 6:
    contador_seis += 1
    
if dado3 == 6:
    contador_seis += 1
    
print(f"Has encontrado un total de {contador_seis} seises")

if contador_seis == 3:
    print("Usted ha obtenido un resultado excelente")

elif contador_seis == 2:
    print("Usted ha obtenido un resultado muy bueno")
    
elif contador_seis == 1:
    print("Usted ha obtenido un resultado regular")

else:
    print("Usted ha obtenido un resultado pésimo")