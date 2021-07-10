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

# Función input():
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