# Nombre del programa: Conversor de moneda.

# El siguiente programa busca convertir pesos méxicanos a dolares. La persona prodra ingresas la cantidad de pesos méxicanos que tenga y el programa le dira su equivalencia en dolares.

pesos = input("¿Cuántos pesos méxicanos tienes?: ")
pesos = float(pesos)
valor_dolar = 19
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")