# Nombre del programa: Dime tú altura.

altura = float(input("Escribe tu altura en centímetros: "))

if altura < 170:
    print("Chaparro")
elif altura >= 170 and altura < 180:
    print("Alto")
else:
    print("Muy alto")