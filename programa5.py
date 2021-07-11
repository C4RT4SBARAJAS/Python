# Nombre del programa: Funciones

# def mi_funcion():
#     print("Bienvenido al curso")
#     print("Ingresa tu nombre: ")

# mi_funcion()
# mi_funcion()
# mi_funcion()

opcion = int(input("Elige una opción (1, 2, 3): "))

def respuestas(mensaje):
    print("Hola")
    print("Muchas felicidades")
    print(mensaje)
    print("Hasta luego")

if opcion == 1:
    respuestas("Elegiste la opción 1")
elif opcion == 2:
    respuestas("Elegiste la opción 2")
elif opcion == 3:
    respuestas("Elegiste la opción 3")
else:
    print("Escriba una opción correcta")