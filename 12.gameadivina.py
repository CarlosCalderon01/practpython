#Fecha-->"11 de octubre del 2022"
#Curso-->"Curso Basico De Python By Facundo garcia Martoni"
#Clase-->"Proyecto: videojuego 27/32"

import random

def run():

    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un del 1 al 100: '))

    while numero_aleatorio != numero_elegido:

        if numero_elegido < numero_aleatorio:
            print('Busca un numero mas grande')

        elif numero_elegido > numero_aleatorio:
            print('Busca un numero menos grande')

        numero_aleatorio = int(input('Elige otro numero: '))
        break;

    print('¡Ganaste!')

if __name__ == "__main__":
    run()
