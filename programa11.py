# Nombre del programa: Prueba de primalidad.

def es_primo(numero):
    contador = 0
    
    for i in range(numero):
        if numero % (i+1) != 0:
            continue
        else:
            contador +=1
    if contador == 2:
        print('Es primo')
    else:
        print('No es primo')  


def run():
    numero = int(input('Ingrese un número: '))
    es_primo(numero)


if __name__ == '__main__':
  run()
