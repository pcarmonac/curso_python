mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {6,7,8,9,0}
print(type(otro_set))
print(otro_set)

print(len(mi_set))
print(2 in mi_set)

s3 = mi_set.union(otro_set)
print(s3)

mi_set.add(6) # agrega un elemento
mi_set.remove(2) # elimina un elemento
mi_set.discard(0) # elimina elemento pero si no existe no arroja error
mi_set.pop() # en este caso elimina un elemento al azar, puede servir para realizar un sorteo
mi_set.clear() # borra y elimina todo el contenido del set
