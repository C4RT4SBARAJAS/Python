# Nombre del programa: Conversor de moneda méxicana.

# El siguiente programa busca convertir pesos méxicanos a dolares. La persona prodra ingresas la cantidad de pesos méxicanos que tenga y el programa le dira su equivalencia en dolares.

pesos = input("¿Cuántos pesos méxicanos tienes?: ")
pesos = float(pesos)
valor_dolar = 20
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")