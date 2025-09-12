#ejercicio 2.20
#creación del diccionario
calificaciones={
    "Liliana": 4.5,
    "Carmen": 3.3,
    "Josefina": 4.1,
    "Daniela": 4.9,
    "Pedro": 2.9,
    "José": 4.6,
    "Mario": 3.3}

# 2. Comprobar el tipo de objeto
print("El tipo de objeto de 'calificaciones' es:", type(calificaciones))

# 2.21 Utilizar la función sorted() para ordenar las claves
nombres_ordenados = sorted(calificaciones.keys())

print("Nombres de los estudiantes ordenados alfabéticamente:")
print(nombres_ordenados)

#2.22
calificaciones.popitem({'Daniela':
4.9}) 
# esta funcion no acepta los argumentos porque su función es eliminar el ultimo valor del diccionario, sin necesidad de especificar cual se va eliminar

#2.23

# Aplicamos el método .items()
items_del_diccionario = calificaciones.items()

print(items_del_diccionario)
print(type(items_del_diccionario))
# items. retorna un Este objeto contiene todos los pares de clave-valor 
# #del diccionario, presentados como una secuencia de tuplas.

#2.24

# Usamos el método .update() para modificar la nota de Liliana
calificaciones.update({"Liliana": 4.7})

# Imprimimos el diccionario para verificar el cambio
print(calificaciones)
#hola
print(f' el resultado de las calificaiones es {calificaciones}')
