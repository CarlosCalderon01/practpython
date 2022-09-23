#Fecha-->"9 de septiembre del 2022"
#Curso-->"Curso Basico De Python By Facundo garcia Martoni"
#Clase-->"Modularizando nuestro conversor de monedas 17/32"

from pprint import pprint


def suma(a, b):
    print('se suman dos variables')
    res = a + b
    return res

sumatoria = suma(1, 4)

print(sumatoria)

#//----------//----------//----------//----------//

menu = """
//-----//Welconme To The Convert Money$//-----//

1- Pesos Colombianos[COP]
2- Pesos Argentinos [ARG]
3- Pesos Mexicanos  [MXC]

//-----//Welconme To The Convert Money$//-----//
"""

def conversor (tipo_pesos, valor_dolar):
    valor = input ("Cuantos Pesos "+ tipo_pesos +" tienes?")
    valor = float(valor)
    dolares = valor/valor_dolar
    dolares = str(dolares)
    print ("Su valor convertidos a dolares es igual a "+dolares+"$")

opcion = int(input(menu))

if opcion == 1:
    conversor ("Colombiano[COP]",3875)

elif opcion == 2:
    conversor ("Argentinos [ARG]", 65)

elif opcion ==3:
    conversor ("Mexicanos [MEX]", 24)

else:
    print ("Ingrese solos llos valores permitidos")