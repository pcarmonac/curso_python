mi_tuple = (1,2,3,4)

print(type(mi_tuple))
print(mi_tuple[0])
print(mi_tuple[-2])

mi_tuple = (1,2,(10,20,30),3,4)
print(mi_tuple[2][0])

# esta asignacion se puede hacer con la tuples y las listas siempre y cuando la cantidad de valores coincidan
t = (1,2,3)
x,y,z = t

print(x,y,z)

t = (1,2,3,1)
print(len(t))

print(t.count(1)) # cuenta cuantas veces aparece un valor dentro del tuple
print(t.index(2)) 