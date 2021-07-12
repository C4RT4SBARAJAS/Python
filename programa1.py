# Nombre del programa: Conversor de moneda méxicana, colombiana, argentina a dolares.

# El siguiente programa busca convertir pesos méxicanos, colombianos, argentinos a dolares. La persona prodra ingresas la cantidad de pesos que tenga según su país y el programa le dira su equivalencia en dolares.

# Función para el conversor.
def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos mexicanos
2 - Pesos colombianos
3 - Pesos argentinos

Elige una opción escribiendo el número: """

opcion = int(input(menu))

if opcion == 1:
    conversor("mexicanos", 20)
elif opcion == 2:
    conversor("colombianos", 3875)
elif opcion == 3:
    conversor("argentinos", 65)
else:
    print("Ingrese una opción correcta")