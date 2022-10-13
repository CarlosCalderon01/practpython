#//-----//-----//-----//-----//-----//-----//-----//-----//

# Lo aprendido en el curso básico de Python;

# 1-) Operadores aritméticos, lógicos y de comparación:

    # 1.1-) Operadores aritméticos.
        
        # { + , - , * , / , ** }

    # 1.2-) lógicos.
        
        # { || , && }

    # 1.3-) comparación.
        
        # { < , > , <= , >= , != , == }

# 2-) Variables y constantes:

    # 2.1-) Variables.

        # int(var) variable a entero.
        # float(var) variable a flotante.
        # str(var) variable a texto.
        # bool(var) variable a booleano.
        # abs(var) variable a valor absoluto.

    # 2.2-) Constantes:
        
        # VARIABLE = 100 # poner una varaible  en mayuscula, la vuelve una constante

# 3-) Funciones y parámetros:

    #3.1-) Funciones.

        # def namefuncion()
        # note: importante retornar y modularizar.

    #3.2-) Parámetros.

        # def namefuncion(parametros):

# 4-) Condicionales:
    
    # 4.1-) if , elif , else

        # if --> (Si) se usa para la condición principal.
        # elif --> (Si no) en caso de que la condición principal o anterior no se cumpla, se puede utilizar para agregar otra condición.
        # else --> (Sino) en caso de que la(s) condición(es) anterior(es) no se cumplan, se ejecuta como alternativa sin condicional.

# 5-) Ciclos, break y continue.

    # 5.1-) Types Of Cycles

        # { for in case , while, }

    # 5.1.2-) For in case.

        # numeros = [18,50,90,-20,100,80,37]
        # for n in numeros:
        #     print(n)
    
        # for contador in range (10): # imprime todos los datos del 0 al 10.
        # for contador in range (1,10): # imprime todos los datos del 1 al 10.
        # print(contador1)

    # 5.1.2-) While.

        #   x = 1
        #   while x < 5:
        #       print(x)
        #       x += 1

        # LIMITE = 100 # poner una varaible  en mayusculas, la vuelve una constante
        # contador = 0
        # while contador < LIMITE:

# 6-) Cadenas.

    #6.1-)Tipos de cadenas.

        # { '' , "" , """ } Note: always open and close with the same quotes.

    # 6.2-) How to edit Character String

        #   nombre = nombre.upper();            # Coloca todo el texto en mayuscula
        #   nombre = nombre.capitalize();       # Coloca primera en mayus
        #   nombre = nombre.strip();            # Elimina espacio del inicio y final sobrantes
        #   nombre = nombre.lower();            # Pone todo en minus
        #   nombre = nombre.replace('o','a')    # Reemplaca todas las o por una a
        #   nombre[0]                           # Acceder a un caracter en especifico
        #   len(nombre)

    # 6.3-) Slice In Character String.

        # Cuando pones [0:3] señalas 3 caracteres desde el inicio hasta el tercero
        # Cuando dejas  vacio señalas inicio o final.
        # [3:] del tres al final.
        # [:3] del inicio hasta el tres.
        # [1:7:2] va el 1 al 7 de 2 en 2.
        # [::] de ini-fin de 1 en 1.
        # [::-1] recorre pero al reves.

# 7-) Listas , Tuplas , Diccionarios.

    # 7.1-) Listas --> las listas utilizan [] editables, Mutables.

        # agregar un objeto a la lista con                                          --> .append()
        # borrar el elemento, no la posicion si no el valor                         --> .pop()
        # Métodos adicionales para listas                                           --> .sorted()
        # También ordena como sort() pero modifica la lista inicial                 --> .clear()
        # Vacía la lista                                                            --> .count()
        # Cuenta las veces que esta un elemento en lista                            --> .index()
        # Indica la posición donde esta un elemento de la lista                     --> .insert()
        # Inserta un elemento en una posición dada ej: lista.insert(posición,item)  --> .reverse()

    # 7.2-) Tuplas --> las Tuplas utilizan () No Editables, Inmutables.

    # 7.3-) Diccionario --> las Diccionario utilizan {} Son Objetos.


#//-----//-----//-----//-----//-----//-----//-----//-----//

# Consejos:

    # Ctrl + / ----> comenta todo lo subrayado

    #todos los datos de entrada se registran como string

    #Siempre despues de poner dos puntos y hacer un salto de linea debemos hacer un tad sangria

    #Siempre es de buena practicar utilizar esta funcion.

    #   if __name__ == '__main__':
    #       run ()

#//-----//-----//-----//-----//-----//-----//-----//-----//