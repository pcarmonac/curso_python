# # nombres=['juan','Ana','Carlos','Belen','Fran']
# # for elemento in nombres
# #         print("Hola" + elemento)

# lista = ['a','b','c']

# for letra in lista:
#         print("letra " + letra)

# lista = ['a','b','c','d']

# for letra in lista:
#         numero_letra = lista.index(letra) + 1
#         print(f"Letra {numero_letra}: {letra}")

# lista = ['pablo','laura','fede','luis','julia']

# for nombre in lista:
#         if nombre.startswith('l'):
#                 print(nombre)
#         else:
#                 print("Nombre que no comienza con L")

# numeros = [1,2,3,4,5]
# mi_valor = 0

# for numero in numeros:
#         mi_valor = mi_valor + numero
#         print(mi_valor)

# palabra = 'python es genial'

# for letra in palabra:
#         print(letra)

# for a,b in [[1, 2], [3, 4], [5, 6]]:
#         print(a)
#         print(b)

# dic = {'clave1':'a','clave2':'b','clave3':'c'}

# for item in dic.items():
#         print(item)

# for a,b in dic.items():
#         print(a,b)

# EJERCICIOS

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for num in lista_numeros:
    suma_numeros = suma_numeros + num
print(suma_numeros)

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0 

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero

print(suma_pares)
print(suma_impares)
