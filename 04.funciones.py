#Fecha-->"9 de septiembre del 2022"
#Curso-->"Curso Basico De Python By Facundo garcia Martoni"
#Clase-->"Aprendiendo a no repetir código con funciones 16/32"

def imprimir_mensaje():
    print('Mensaje especial: ')
    print('!estoy aprendiendo a usar funciones')

imprimir_mensaje()
imprimir_mensaje()
imprimir_mensaje()

#//-----//-----//-----//-----//-----//-----//-----//-----//

def mensaje_welcome(mensaje):
    print('Welcome, good today')
    print(mensaje)
    print('Good, bye!')

opcion = int(input('Ingresa una de las opciones {1,2,3}'))

if opcion == 1:
    mensaje_welcome('pick, option 1')
elif opcion == 2:
    mensaje_welcome('pick, option 2')
elif opcion == 3:
    mensaje_welcome('pick, option 3')
else:
    print('Ingresa una de las opciones descritas')