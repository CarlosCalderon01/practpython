#Fecha-->"12 de octubre del 2022"
#Curso-->"Curso Basico De Python By Facundo garcia Martoni"
#Clase-->"¿Qué son los diccionarios? 30/32"

# las {} se usan para diccionarios
# las [] se usan para listas dinamicas o mutables
# las () se usan para listas staticas o inmutables

# Los diccionarios en Python son una estructura de datos mutable las cuales almacenan diferentes tipos de valores
# sin darle importancia a su orden. Identifican a cada elemento por una clave (Key). Se escriben entre {}.

# Operaciones en diccionarios

# .keys():Retorna la clave de nuestro elemento.

# .values(): Retorna una lista de elementos (valores del diccionario).

# .items(): Devuelve lista de tuplas (primero la clave y luego el valor).

# .clear(): Elimina todos los items del diccionario.

# .pop(“n”): Elimina el elemento ingresado.

def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }

    # print(poblacion_paises['Bolivia'])

    # for pais in poblacion_paises.keys():
    #     print(pais)

    # for pais in poblacion_paises.values():
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')


if __name__ == '__main__':
    run()
