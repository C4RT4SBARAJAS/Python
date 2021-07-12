# Nombre del programa: Elige una opción.

# Función.
# def mi_funcion():
#     print("Bienvenido al curso")
#     print("Ingresa tu nombre: ")

# mi_funcion()
# mi_funcion()
# mi_funcion()

# Función con un parámetro.
# opcion = int(input("Elige una opción (1, 2, 3): "))

# def respuestas(mensaje):
#     print("Hola")
#     print("Muchas felicidades")
#     print(mensaje)
#     print("Hasta luego")

# if opcion == 1:
#     respuestas("Elegiste la opción 1")
# elif opcion == 2:
#     respuestas("Elegiste la opción 2")
# elif opcion == 3:
#     respuestas("Elegiste la opción 3")
# else:
#     print("Escriba una opción correcta")

# Función con dos parámetros.
def suma(a, b):
    print("Se suman dos números")
    resultado = a + b
    return resultado

sumatoria = suma(1, 4)
print(sumatoria)