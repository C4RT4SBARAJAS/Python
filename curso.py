# Bienvenido al curso de Python desde cero.

# NOTA: Esta es un scrip de cálculos, si quieres saber más a detalle sobre cada punto, revisa el arvhico curso.txt adjunto.

# Operaciones artiméticas básicas en Python.
# NOTA: Estos cálculos son realizados utilizando la consola, en caso de usar un editor de código usar la función print() para visualizar los resultados:
# Suma
5 + 5

# Resta
10 - 2

# División
25 / 5

# Cociente de una división
25 // 5

# Residuos de una división
25 % 5

# Potencia
3**2

# Raíz cuadrada
25 ** 0.5

# Variables en Python.
# nombre_variable = contenido

# Tipos de datos en Phyton.
# Datos númericos (integers)

var1_num = 5

# Datos decimales

var2_num = 3.5

# Datos de caracteres (strings)

var1_str = "Heriberto"
var2_str = 'Cartas'
var3_str = "Barrera"

# Datos booleanos

var1_boo = True
var2_boo = False

# Operaciones con cadena de caracteres.
# Definimos tres variables donde la primera guradará el nombre de una persona, la segunda el primer apellido y la tercera el segundo apellido.
nombre = "heriberto"
apellido1 = "cartas"
apellido2 = "barrera"

# Podemos sumar caracteres logrando formar cadenas:
nombre + apellido1 + apellido2

# Podemos agregar espacios de la siguiente manera y guardar en una variable:
nombre_completo = nombre + " " + apellido1 + " " + apellido2

# Métodos en Python.
# Un método es una función para un tipo de dato en particular que tiene la siguiente sintaxis en python:
# dato_tipo.nombre_función()

# Cambiar el texto a Mayusculas en la variable nombre:
nombre.upper()

# Colocar la primera letra en Mayusculas en las tres variables, y sobreescribiendo la variable:
nombre = nombre.capitalize()
nombre = apellido1.capitalize()
nombre = apellido2.capitalize()

# Eliminar espacios basura al inicio o final:
nombre = "heriberto "
nombre.strip()

# Cambiar el texto a minusculas:
nombre = "HERIBERTO"
nombre.lower()

# Remplazar una letra por otra, utilzando párametros:
nombre = "heriberto"
nombre.replace("o", "a")

# Índices en Python.
# Permiten devolver una letra en específico de una cadena. Presentando la siguente sintaxis:
# dato_tipo_string[algún dígito contando desde el 0]

# Devolviendo la primera letra de la variable nombre:
nombre = "heriberto"
nombre[0]

# Devolviendo la última letra de la variable nombre:
nombre[8]

# Función len().
# Pemite devolver la longitud de un dato_tipo_string. Es decir, cuantas letras existen en mi variable nombre por ejemplo:
nombre = "heriberto"
len(nombre)
len("Bienvenido al curso de Python desde cero")

# Slices en Python.
# Los slices en python hacen referencia a rebanadas, donde puedes cortar una cadena de caracteres en las partes que desees. Para ello necesitamos conocer el número de letras que formar el string:
nombre = "heriberto"
nombre[0:4]

# Partiendo en dos rebanadas el string "heriberto":
nombre[:4]
nombre[4:]

# Podemos agregar un número más que representarían los pasos o separaciones en las reabanadas. Por ejemplo, quiero una rebanada que valla del uno al siete, pero con una separación de dos en dos:
nombre[1:7:2]

# Obteniendo el string completo:
nombre[::]

# Obteniendo el string de forma inversa o al reves:
nombre[::-1]

# Función input().
# Esta función te permite agregar datos a tus variables de forma más cómoda
edad1 = input("Ingresa tu edad: ")
edad2 = input("Ingresa tu edad: ")

# Cambiar un tipo de datos a otro tipo en Python
# Cabiar un datos de tipo caracter a númerico usando la función int()

edad1 = "21"
edad2 = int(edad1)

# Cabiar un decimal a un entero usando la función int()
edad2 = "21.9"
edad2 = int(edad2)

# Cambiando un númerico a string usando la función str()
str(edad1)

# Operadores lógicos
# Definamos dos variables que describen la situación de un estudiante llamado Heriberto: 
estudia = True
trabaja = False

# Realizando algúnas preguntas sobre Heriberto:
# 1. ¿Heriberto estudia y trabaja?
estudia and trabaja
# 2. ¿Heriberto estudia o almenos trabaja?
estudia or trabaja

# Invirtiendo el valor de las variables
not estudia
not trabaja

# Operadores de comparación
# Definamos 3 variables que guardan las edades de tres personas diferentes:
heriberto = 21
erika = 21
arlet = 19

# Realizando algúnas preguntas sobre las edades:
# 1. ¿La edad de heriberto es igual a la edada de erika?
heriberto == erika
# 2. ¿La edad de heriberto es mayor que la edad de erika?
heriberto > erika
# 3. ¿La edad de erika es menor a la edad de arlet?
erika < arlet
# 4. ¿La edad de erika es mayor o igual a la edad de arlet?
erika >= arlet
# 5. ¿La edada de arlet es menor o igual a la edad de heriberto?
arlet <= heriberto
# 6. ¿La edad de erika es distinta a la edad de heriberto?
erika != heriberto

# Condicionales en Python.
# Definamos 2 respuestas en base a mi edad, teniendo en cuenta que tengo 21 años. Sí mi edad es menor a 18 años entonces soy menor de edad y sí no entonces soy mayor de edad.

mi_edad = 21
# Una condicional en python luce de la siguiente manera:
if mi_edad < 18:
    print("Soy menor de edad")
else:
    print("Soy mayor de edad")

# Condicionales booleanas en Python.
# Definamos 3 respuestas de acuerdo a mi estatura en centímetros, considerando que mido 170 cm. Sí mi estatura es menor a 170 cm entonces soy chaparro, sí mi estatura esta entre los 170 y 179 cm entonces soy alto, y sí no es que soy muy alto.

mi_estatura = 170
# La condicional luce de la siguiente manera:
if mi_estatura < 170:
    print("Soy chaparro")
elif mi_estatura >= 170 and mi_estatura <= 169:
    print("Soy alto")
else:
    print("Soy muy alto")

# Funciones en Python.
# A continuación, repetimos dos líneas de codigo intencionalmente.
print("Ingresa tu nombre: ")
print("Comentarios: ")
print("Ingresa tu nombre: ")
print("Comentarios: ")
print("Ingresa tu nombre: ")
print("Comentarios: ")

# Las funciones nos evitan repetir líneas de código guardando ese código en funciones que nosotros mismos creamos. Las funciones son una buena práctica. Nuestra función se vería así:
def mi_funcion():
    print("Ingresa tu nombre: ")
    print("Comentarios: ")

# Para ejectur estas lineas de código llamamos a al función el número de veces que queramos:
mi_funcion()
mi_funcion()
mi_funcion()

# Parámetros en una función.
# Los parámetros funcionan como variables dentro de una función, es el mensaje que cambia. 

# A continuación, repetimos 4 líneas de codigo intencionalmente.
print("Hola")
print("Muchas felicidades")
print("Elejiste la opción 1")
print("Hasta luego")
print("Hola")
print("Muchas felicidades")
print("Elejiste la opción 2")
print("Hasta luego")
print("Hola")
print("Muchas felicidades")
print("Elejiste la opción 3")
print("Hasta luego")

# Como pudiste observar hay 3 líneas de códigos comunes en cada repetición.
# Ahora escribamos este código de una forma más corta usando una función y un parámetro:
def respuestas(mensaje):
    print("Hola")
    print("Muchas felicidades")
    print(mensaje)
    print("Hasta luego")

# Para generar el bloque de código de 4 líneas llamamos a la función creada, modificando unicamente el parámetro mensaje:
respuestas("Elegiste la opción 1")
respuestas("Elegiste la opción 2")
respuestas("Elegiste la opción 3")