#Fecha-->"9 de septiembre del 2022"
#Curso-->"Curso Basico De Python By Facundo garcia Martoni"
#Clase-->"Construyendo el camino de un programa con condicionales 14/32"

#Ejemplos 1

edad = int(input("escribe tu edad: "))

if edad >= 20:
    print (("Es mayor de edad"))
else:
    print("Es menor de edad")

#//-----//-----//-----//-----//-----//-----//-----//-----//

numero = int(input("escribe tu numero: "))

if numero > 5:
    print (("Es mayor de a cinco"))
elif numero == 5:
    print ("es igual a cinco")
else:
    print("Es menor a cinco")

#//-----//-----//-----//-----//-----//-----//-----//-----//

#Notas:
# Ctrl + / ----> comenta todo lo subrayado
# Tipos de condicionales { <, >, <=, >=, !=, ==, ===, ||, &&}
# Type {if, ellif, else}
#Siempre despues de poner dos puntos y hacer un salto de linea debemos debemos hacer un tad sangria

#//-----//-----//-----//-----//-----//-----//-----//-----//

# Un detalle muy importante en cualquier lenguaje de programación es conocer las diferencias entre los condicionales. En Python en particular, es crucial mencionar la diferencia entre if, elif y else.

# Diferencias entre if, else y elif
# if:
# if se encarga de iniciar el condicional y solicitar un requisito para ejecutar todo el código por debajo, que conocemos como bloque de código.

# else:
# Si se desea ejecutar otro código en caso de que no se cumpla el if. Por ejemplo: el usuario no elige la opción 1, entonces (else)…

# elif:
# Se utiliza cuando utilizamos múltiples condiciones, lo que en el código de esta clase son la opción 2 y 3. En esta clase, teníamos la opción 1, pero debemos también evaluar qué pasa si el usuario elige la opción 2 o 3, por lo que decimos “que estamos evaluando múltiples condiciones”.

# Los condicionales son decisiones que se establecen desacuerdo a los parámetros que indiquemos, para obtener un tipo de resultado deseado.

# Ejemplo: si un número es mayor o igual que otro, los números deberán sumarse, de lo contrario deberán restarse. Debe cumplirse una condición para saber cuál será el camino a seguir.

# A continuación veremos cómo funcionan los condicionales en Python.

# if
# (Si) se usa para la condición principal.

# elif
# (Si no) en caso de que la condición principal o anterior no se cumpla, se puede utilizar para agregar otra condición.

# else
# (Sino) en caso de que la(s) condición(es) anterior(es) no se cumplan, se ejecuta como alternativa sin condicional.

# En lenguaje natural (español)
# ‘Si’ introduce una oración en la que se indica una condición real o hipotética que se ha de cumplir necesariamente para que sea cierto o se produzca lo que se expresa: Si corres, lo alcanzarás.

# ‘Sino’ es una conjunción adversativa que se escribe en una sola palabra y se usa, principalmente, para contraponer un concepto a otro: No estudia, sino que trabaja.

‘Si no’** introduce una oración condicional: Si no estudias, no aprobarás.

