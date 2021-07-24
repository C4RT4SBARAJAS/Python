# Nombre del programa: Diccionario.

# Mirando el contenido del diccionario:
# def run():
#     mi_diccionario = {
#         'llave1': 1,
#         'llave2': 2,
#         'llave3': 3
#     }
#     print(mi_diccionario)

# Mirando el contenido de cada elemento:
# def run():
#     mi_dicionario = {
#         'llave1': 1,
#         'llave2': 2,
#         'llave3': 3
#     }
#     print(mi_dicionario['llave1'])
#     print(mi_dicionario['llave2'])
#     print(mi_dicionario['llave3'])

# Ejemplo con países:
def run():
    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }
    # print(poblacion_paises['Argentina'])

    # for pais in poblacion_paises.keys():
    #     print(pais)

    # for pais in poblacion_paises.values():
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')

if __name__ == '__main__':
    run()