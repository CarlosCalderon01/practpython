#Fecha-->"4 de octubre del 2022"
#Curso-->"Curso Basico De Python By Facundo garcia Martoni"
#Clase-->"Aprendiendo bucles 21/32 - 23/32"

#//--------------------//WHILE-mientras//--------------------// 22/32
#ejecutar mientras se cumpla con la condicion:
def run():
    LIMITE = 100 # poner una varaible  en mayusculas la vuelve una constante
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador


#//--------------------//For//--------------------// 23/32
# imprime todos los datos  del 1 al 10
def funcion_for1():
    for contador1 in range (1,10):
        print(contador1)
#//-----//-----//-----//-----//-----//-----//-----//
# imprime todos los datos  del 1 al 101
def funcion_for2():
    for i in range (1, 10):
        print(11 * i)
#//-----//-----//-----//-----//-----//-----//-----//

#apuntes

#   a = list(range(1000)) <<---- hace una lista de 0 a 10000

#//--------------------//For-recorrrer string//--------------------// 24 y 25 /32

def recorrer_string():
    # nombre = input("escribe el nombre")
    # for letra in nombre:
    #     print(letra)

    frase = input ("escribe la frase: ")
    for caracter in frase:
        print (caracter.upper())


#entry point
if __name__ == '__main__':
    #run()
    #funcion_for1()
    recorrer_string()