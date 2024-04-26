mi_lista = ["a","b","c"]
mi_lista2 = ["d","e","f"]

print(type(mi_lista))

resultado = len(mi_lista)
print(resultado)

indice = mi_lista[0]
print(indice)

indice_2 = mi_lista[0:2]
print(indice_2)

print(mi_lista + mi_lista2) # concatenacion

mi_lista3 = mi_lista + mi_lista2
print(mi_lista3) # concatenacion

mi_lista3[0] = "alfa" # reemplaza elementos de la lista
print(mi_lista3)

mi_lista3.append("g") # agrega elementos a la lista
print(mi_lista3)

eliminado = mi_lista3.pop() # interpreta que debe eliminar el ultimo elemento y lo guarda en la variable
print(mi_lista3)
print(eliminado)

lista = ["g","o","m","c","b"]
lista.sort() # ordena in situ, no puede guardar los datos de orden
print(lista)

lista.reverse() # ordena in situ, no puede guardar datos del orden inverso.
print(lista)
