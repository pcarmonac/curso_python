lista = ['a','b','c']
indice = 0

for item in lista:
    print(indice,item)
    indice = indice + 1

lista = ['a','b','c']

for item in enumerate(lista):
    print(item)

#de manera directa rescato el indice e item directo de la lista
lista = ['a','b','c']

for indice,item in enumerate(lista):
    print(indice,item)

#No necesito usar una lista que contenga los numeros, los rescato directo de un range
for indice, item in enumerate(range(50,61)):
    print(indice,item)

#EJERCICIO 1
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

#EJERCICIO 2
nombre = "Python"

mi_tuples = list(enumerate(nombre))
print(mi_tuples)

#EJERCICIO 3
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

nombres = list(enumerate(lista_nombres))
print(lista_nombres)