#Fecha-->"12 de octubre del 2022"
#Curso-->"Curso Basico De Python By Facundo garcia Martoni"
#Clase-->"¿Qué son los diccionarios? 30/32"

# las {} se usan para diccionarios
# las [] se usan para listas dinamicas o mutables
# las () se usan para listas staticas o inmutables

def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3
    }
    poblaciones = {
        'argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }

    diccionario = {
        'Red': 'Rojo',
        'Blue': 'Azul',
        'Green': 'Verde',
    }

    #print(str(diccionario['Green']))
    print(diccionario)

if __name__ == '__name__':
    run()
    