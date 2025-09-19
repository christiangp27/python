
#definicion
#uso de palabras reservada def
#nombre 
#parametros

def mi_función():
    #instrucciones
    return True

#uso 
#llamados a la función enteegandole datos en los argumentos
print(mi_función())

import random

def mi_aleatorio():
    return random.randint(1,100)

print(mi_aleatorio())

def mi_aleatorio_2(a,b):
    return random.randint(a,b)

print(mi_aleatorio_2(8,50))


x=90
y=100

def multiples_retornos():
    z=50
    return x,y,z

print(multiples_retornos())
#print(x,y,z) #las variables definidas dentro de una función solo viven en ellas

#funciones con parametros opcionales
def otra_funcion(a=True):
    return print ("por defecto será True", "actualmente es",a)

#llamo a la funcion
otra_funcion(False)
