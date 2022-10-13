#Fecha-->"11 de octubre del 2022"
#Curso-->"Curso Basico De Python By Facundo garcia Martoni"
#Clase-->"PAlmacenar varios valores en una variable: listas 28/32"

#objetos.append(1) agregar un objeto a la lista con .append

#objetos.pop(1) borrar el elemento 1, no la posicion si no el valor

# Métodos adicionales para listas
# .sorted()
# También ordena como sort() pero modifica la lista inicial
# .clear()
# Vacía la lista
# .count()
# Cuenta las veces que esta un elemento en lista
# .index()
# Indica la posición donde esta un elemento de la lista
# .insert()
# Inserta un elemento en una posición dada ej: lista.insert(posición,item)
# .reverse()
# Le da la vuelta a una lista


numeros = [1,2,3,4,5]

numeros2 = [6,7,8,9]

lista_final = numeros + numeros2

print(lista_final)

mi_tupla = (1,2,3,4,5)
#las listas son objetos dinamicos que se pueden editar, mutables
#las tuplas son objetos staticos Note: no se pueden agregar elementos, ni quitar,  son inmutables.

for numeros in mi_tupla:
    print(numeros)



