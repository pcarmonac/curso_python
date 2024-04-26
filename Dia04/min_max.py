menor = min(58,96,72,64,35)
mayor = max(58,96,72,64,35)

print(menor,mayor)

lista = [58,96,72,64,35]

print(f"El menor es {min(lista)} y el mayor es {max(lista)}")

nombres = ['juan','alicia','pablo','carlos']

print(f"El menor nombre es {min(nombres)} y el mayor es {max(nombres)}")

nombre = "Carlos" #ojo que min y max buscan primero en las mayusculas y despues en minusculas, usar .lower

print(min(nombre.lower()))

dic = {'C1':45,'C2':11}

print(min(dic.values())) #ojo que si quiero que me entre el valor dentro del diccioanrio mas pequeño debo usar el metodo .values

# Ejercicio 1
# Obtener el valor maximo

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

valor_maximo = max (lista_numeros)

# Ejercicio 2
# diferencia entre valor max y el min

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

rango = max(lista_numeros) - min(lista_numeros)

# Ejercicio 3
# Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente diccionario:
# También, obtén el nombre que se ubica último en orden alfabético, y almacénalo

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())

print(edad_minima,ultimo_nombre)