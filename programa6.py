# Nombre del programa: Palíndromo.
# El programa trata de averiguar si una palabra es un palíndromo o no.
# Un palíndromo es una palabra que se lee igual al derecho y al reves, pudiendo ser tanto una palabra como una frase.

def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindrono = palindromo(palabra)
    if es_palindrono == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


if  __name__ == '__main__':
    run()