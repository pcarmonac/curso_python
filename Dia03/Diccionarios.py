diccionario = {'c1':'valor1','c2':'valor2'} # los valores se pueden repetir, pero no a si las claves
print(type(diccionario))

print(diccionario)

resultado = diccionario['c1']
print(resultado)

cliente = {'nombre':'Juan','apellido':'Fuentes','peso':85,'Talla':1.76}
consulta = cliente['apellido']
print(consulta)

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c2'][1])
print(dic['c3']['s2'])

# Ejercicio
dic = {'c1':['a','b','c'],'c2':['d','e','f']}
letra = dic['c2'][1]

print(letra.upper())
print(dic['c2'][1].upper())

# agregar elementoa a diccionario creado
dic = {1:'a',2:'b'}
print(dic)

dic[3] = 'c'
print(dic)

dic[2] = 'B' # reemplazo una clave por otra
print(dic)

print(dic.keys()) # keys imprime las claves
print(dic.values()) # values imprime los valores del diccionario
print(dic.items()) # trae todos los elementos dentro del diccionario
