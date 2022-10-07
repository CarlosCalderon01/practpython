#Fecha-->"6 de octubre del 2022"
#Curso-->"Curso Basico De Python By Facundo garcia Martoni"
#Clase-->"Interrumpiendo ciclos con break y continue 25/32"

from typing import TextIO


def run ():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range (10000):
    #     print (i)
    #     if i == 5678:
    #         break

    Texto = input("escribe algo")
    for letra in Texto:
        if letra == 'o':
            break
        print(letra)

if __name__ == '__main__':
    run()