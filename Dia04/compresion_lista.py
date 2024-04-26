# manera convencional de como hacer una lista a partir de un string
palabra = 'python'
lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

# usar menos codigo para hacer la lista a partir del string
palabra = 'python es lo maximo'

lista = [letra for letra in palabra]

print(lista)

# mas directo
lista = [letra for letra in 'python']

print(lista)

# una lista a partir de numeros
lista = [n for n in range(0,50,2) if n * 2 > 10] # creo una lista de numero en un rango de 0 a 50 con un salto de 2 en 2 y el numero se guarda siempre y cuando al multiplicar por 2 se mayor que 10

print(lista)

# como tener una lista en pies y crear una lista convertida a metros
pies = [10,20,30,40,50]
metro =[p * 3.281 for p in pies]

print(metro)

# Ejercicio 1
# Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [v ** 2 for v in valores]

# Ejercicio 2
# Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [v for v in valores if v %2 == 0]

# Ejercicio 3
# Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos valores en una nueva lista de valores de temperatura en grados Celsius.

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(g-32)*(5/9) for g in temperatura_fahrenheit]