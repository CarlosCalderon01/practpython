#Fecha-->"4 de octubre del 2022"
#Curso-->"Curso Basico De Python By Facundo garcia Martoni"
#Clase-->"Proyecto: palíndromo 20/32"

#palindromo son palabras que se leen igual al derecho y al reves.
def palindromo(palabra):
    palabra = palabra.replace(" ","") #eliminar el espacios vacios    
    palabra = palabra.lower() #eliminar mayusculas
    palabra_invertida = palabra[::-1] # invertir palabra
    if palabra == palabra_invertida: # Compararlas
        return True 
    else:
        return False

def run():
    palabra = input('Escriba una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo ==True:
        print('Es palindromo')
    if es_palindromo == False:
        print('No es palindromo')

if __name__ == '__main__':
    run()
