# Nombre del programa: Conversor de moneda méxicana, colombiana, argentina a dolares.

# El siguiente programa busca convertir pesos méxicanos, colombianos, argentinos a dolares. La persona prodra ingresas la cantidad de pesos que tenga según su país y el programa le dira su equivalencia en dolares.

menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos mexicanos
2 - Pesos colombianos
3 - Pesos argentinos

Elige una opción escribiendo el número: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cuántos pesos méxicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 20
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion == 2:
    pesos = input("¿Cuántos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion == 3:
    pesos = input("¿Cuántos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
else:
    print("Ingrese una opción correcta")