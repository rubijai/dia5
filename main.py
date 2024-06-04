#   Unidad 5: Funciones
#   Cuando una tarea determinada se realiza muchas veces a lo largo de un programa, generalmente se encapsula
#   dentro de una función para que pueda ser utilizada o "llamada" cuando sea necesario. Esta noción de
#   crear una función específica o "procedimiento" para lograr una tarea determinada es parte de una
#   metodología de programación conocida como "programación por procedimientos".

#   Las funciones son útiles cuando tenemos una sección de código que necesitamos usar una y
#   otra vez. Al poner la sección de código en forma de función, permitimos la reutilización
#   del código al llamar a la función. Las funciones reciben valores de entrada,
#   luego realizan un cálculo utilizando la entrada y, finalmente, devuelven valores como resultado de la
#   función. Python tiene muchas funciones incorporadas, como print, type y len
#   (con las que ya tienes experiencia). Por ejemplo, en el caso de la función len,
#   la entrada es una lista y la salida es el número de elementos contenidos en la lista.

#   Los métodos son funciones que se pueden usar con objetos. Ya has utilizado varios
#   métodos asociados con listas (como append) y cadenas (como find). Aprenderemos
#   sobre la creación de métodos cuando lleguemos a la programación orientada a objetos.
#   Pero, cabe destacar que la idea de usar un método es similar a la de una
#   función en el sentido de que los métodos tienen valores de entrada y devuelven valores de salida.

#   Supongamos que tienes una lista de datos numéricos y te gustaría encontrar un valor en esa lista.
#   Supongamos además que tienes un programa que debe realizar este cálculo en muchos
#   puntos diferentes dentro del programa. Bajo estas circunstancias, tiene sentido escribir
#   una función para resolver este problema.

#   Empieza la definicion de la funcion ...

def findval(alist, x):
    #   alist es la lista de entrada
    #   x es el valor que se busca
    #   Esta función devuelve un valor booleano True si se encuentra
    #   y devuelve un valor booleano False si no se encuentra.
    for val in alist:
        if (val == x):
            return True
    return False


#   termina la definicion de la funcion
#   =====================
#   aqui empieza el codigo principal ...

a = [2, 3, 4, 5, 6, 7, 8]
print(findval(a, 4))
print(findval(a, 29))
b = [45, 34, 78, 89]
print(findval(b, 45))
print(findval(b, 1470))
print('...........')



#  #  La palabra clave def informa a Python que se está declarando una función.
#  Observa los (:) y la sangría con reglas similares a las sentencias condicionales y
#  bucles. Nombre de la función: El nombre de la función es findval.
#  Entradas: findval tiene dos variables de entrada, alist y x.
#  Salidas: findval devuelve una variable de salida de tipo bool.
#  La palabra clave return se encarga de devolver el valor de salida.

#  Por defecto, las variables utilizadas dentro de la función son locales a la función y gran parte
#  del poder de Python reside en la vasta colección de paquetes, bibliotecas y módulos
#  disponibles para casi cualquier aplicación que puedas imaginar. El módulo math contiene
#  una serie de métodos orientados a las matemáticas, típicos de lo que un programador necesitaría
#  para realizar cálculos básicos. No pueden ser vistos por los comandos principales que siguen.
#  Por convención, las funciones se definen al comienzo de un programa de Python.

import math     # importa el modulo math que contiene las definiciones de las funciones matematicas

# Operaciones básicas:
#
# math.add(x, y): Suma dos números.
# math.subtract(x, y): Resta dos números.
# math.multiply(x, y): Multiplica dos números.
# math.divide(x, y): Divide dos números.
# math.floor(x): Redondea un número hacia abajo al entero más cercano.
# math.ceil(x): Redondea un número hacia arriba al entero más cercano.

# Funciones trigonométricas:
#
# math.sin(x): Calcula el seno de un ángulo en radianes.
# math.cos(x): Calcula el coseno de un ángulo en radianes.
# math.tan(x): Calcula la tangente de un ángulo en radianes.
# math.asin(x): Calcula el arcoseno de un número.
# math.acos(x): Calcula el arcocoseno de un número.
# math.atan(x): Calcula la arcotangente de un número.

# Funciones exponenciales y logarítmicas:
#
# math.exp(x): Calcula la exponencial de un número.
# math.log(x): Calcula el logaritmo natural (base e) de un número.
# math.log10(x): Calcula el logaritmo en base 10 de un número.

# Otras funciones:
#
# math.sqrt(x): Calcula la raíz cuadrada de un número.
# math.pi: Devuelve el valor de pi (π).
# math.e: Devuelve el valor de e.

a = math.exp(1) # se usa la sintaxis  de un metodo del modulo math
print(a)
b = math.pi
print(b)
x = 100
print(math.log(x, 10))
print(math.log10(x))
y = math.pi / 2
print(math.cos(y))
print(math.sin(y))
y = 8
z = 1 / 3
print(math.pow(y, z))



#  Para simplificar el código, si sabes exactamente qué métodos se necesitan de
#  una biblioteca determinada, puedes seleccionar un subconjunto utilizando la palabra clave from.
#  Considera el código anterior reescrito utilizando la palabra clave from:

from math import exp, pi, log, log10, cos, sin, pow

a = exp(1)      # en este caso no es necesario usar la sintaxis a = math.exp(1)
print(a)
b = pi
print(b)
x = 100
print(log(x, 10))
print(log10(x))
y = pi / 2
print(cos(y))
print(sin(y))
y = 8
z = 1 / 3
print(pow(y, z))  # pow es un metodo del modulo math que se encarga de elevar un número  y a la potencia z

#   La capacidad de generar números pseudoaleatorios es fundamental en la programación y simulación.
#   El módulo random ofrece un conjunto de métodos para hacerlo.





import random as rn     # rn es un alias random que permite usar rn en lugar de random en la sintaxis
#Generar números aleatorios:

#random.random(): Genera un número aleatorio flotante entre 0.0 (inclusivo) y 1.0 (exclusivo).
#random.uniform(a, b): Genera un número aleatorio flotante uniformemente distribuido entre a (inclusivo) y b (exclusivo).

#Generar enteros aleatorios:

#random.randint(a, b): Genera un número entero aleatorio uniformemente distribuido entre a (inclusive) y b (inclusive).

#Otras funciones:

#random.choice(secuencia): Elige un elemento aleatorio de una lista, tupla o cadena.
#random.shuffle(lista): Mezcla los elementos de una lista de forma aleatoria.
#random.seed(semilla): Inicializa el generador de números aleatorios con una semilla
# específica para obtener resultados reproducibles (opcional).
#   Fija la semilla al reloj
rn.seed()         # sin alias seria random.seed()

#   prueba algunos metodos
a = rn.random()  #   numero aleatorio entre 0 y 1
print(a)
b = rn.uniform(7, 20)  #   numero aleatorio entre  7  20
print(b)
c = rn.randint(100, 200)  #   entero aleatorio entre 100 y 200
print(c)


#    #  Para mayor comodidad, la palabra clave as junto con el comando import acorta el nombre de
#    la referencia del módulo de random a rn.
#    La "semilla" de un generador de números aleatorios define el punto de inicio. En aplicaciones reales,
#    quieres establecer la semilla en un valor aleatorio (como la hora del reloj del sistema)
#    de lo contrario, una lista pseudoaleatoria siempre comenzará con el mismo valor y se repetirá.
#    Tres métodos esenciales para generar números aleatorios son:
#    random.random() - generar números de punto flotante entre 0 y 1
#    random.uniform(a, b) - generar números de punto flotante entre a y b
#    random.randint(a, b) - generar enteros entre a y b



# *args

def add(*args):  # *args se puede usar cualquier numero de argumentos
    # args es un tuple con cualquier numero de argumentos
    # sum = 0
    # for m in args:
    # sum += m
    return sum(args)      # usa la funcion sum de python
print(add(3, 5, 8, 125))  # el numero de argumentos es ilimitado


def add1(a=1, b=2, c=3):  # tiene 3 argumentos con valores iniciales que pueden cambiarse
    sum = a + b + c
    return sum

print(add(3, 4, 7, 10))  # 24
print(add(3, 4))  # 7
print(add1())  # a=1,b=2,c=3       sum = 6
print(add1(c=100))  # a=1,b=2,c=100  mantiene los valores a y b  sum=103

print(add1(c=7))  # a=1,b=2,c=7  sum = 10




def calculate(n,**kwargs):    # **kwargs keyworded arguments is a dictionary
    for key,value in kwargs.items():
        print(kwargs.items(), type(kwargs.items()))  # --> [('add',3),('multiply',6)] 2 elementos
        print(key)
        print(value)
        print(kwargs[key])
    n = (n + kwargs['add']) * kwargs['multiply']
    print(n)
    n *= kwargs['multiply']
    print(n)
    # kwargs = {'add':3,'multiply':6}
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']
    #print(n)
    return n

print(calculate(5,add=3,multiply=6))





def calculate1(n,**kwargs):
    for key,value in kwargs.items():
        print(kwargs.items(),type(kwargs.items()))    #--> [('add',3),('multiply',6)] 2 elementos
        print(key)
        print(value)
        print(kwargs[key])
        n += kwargs['add']
        print(n)
        n *= kwargs['multiply']
    return n

print(calculate1(5,add=6,multiply=9))
