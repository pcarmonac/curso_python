from random import * # aca importamos lo que necesitamos ocupar ej randint, si queremos importar toda la libreria random usamos *

aleatorio = randint(1,50) # obtenemos un aleatorio integer
print(aleatorio)

aleatorio = round(uniform(1,5),2) # con uniform obtenemos un aleatorio float
print(aleatorio)

aleatorio = random() # elige un numero float entre 0 y 1
print(aleatorio)

color = ['azul','rojo','verde','amarillo'] # choice elige al azar en este caso un color
aleatorio = choice(color)
print(aleatorio)

numeros = list(range(5,50,5)) # shuffle desordena al azar una lista de numeros pero no se puede almacenar
print(numeros)

shuffle(numeros)

print(numeros)
