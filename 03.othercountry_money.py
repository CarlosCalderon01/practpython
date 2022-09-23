#Fecha-->"9 de septiembre del 2022"
#Curso-->"Curso Basico De Python By Facundo garcia Martoni"
#Clase-->"Varios países en mi conversor de monedas 15/32"

menu = """
//-----//Welconme To The Convert Money$//-----//

1- Pesos Colombianos[COP]
2- Pesos Argentinos [ARG]
3- Pesos Mexicanos  [MXC]

//-----//Welconme To The Convert Money$//-----//
"""

opcion = int(input(menu))

if opcion == 1:
    valor = input ("Cuantos Pesos Colombianos[COP] tienes?")
    valor = float(valor)
    valor_dolar = 4000
    dolares = valor/valor_dolar
    dolares = str(dolares)
    print ("Su valor convertidos a dolares es igual a "+dolares+"$")

elif opcion == 2:
    valor = input ("Cuantos Pesos Argentinos [ARG] tienes?")
    valor = float(valor)
    valor_dolar = 300
    dolares = valor/valor_dolar
    dolares = str(dolares)
    print ("Su valor convertidos a dolares es igual a "+dolares+"$")

elif opcion == 3:
    valor = input ("Cuantos Pesos Mexicanos  [MXC] tienes?")
    valor = float(valor)
    valor_dolar = 24
    dolares = valor/valor_dolar
    dolares = str(dolares)
    print ("Su valor convertidos a dolares es igual a "+dolares+"$")

else:
    print ('Por favor, Ingresa Una De Las Opciones Que Esten Registradas')
