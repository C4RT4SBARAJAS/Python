# Nombre del programa: Conversor de dolares.

# El siguiente programa busca convertir dolares a pesos méxicanos. La persona prodra ingresas la cantidad de dolares que tenga y el programa le dira su equivalencia en pesos méxicanos.

dolares = input("¿Cuántos dólares tienes?: ")
dolares = float(dolares)
valor_pesos = 20
pesos = dolares * valor_pesos
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos")