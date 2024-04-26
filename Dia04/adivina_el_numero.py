from random import randint

intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: ")

print(f'Bueno {nombre}, he pensado un numero entre 1 y 100\nTienes 8 intentos para adivinar')

while intentos < 8:
    estimado = int(input('Cual es el numero: '))
    intentos = intentos + 1

    if estimado < numero_secreto:
        print('Mi numero es mas alto')
    
    if estimado > numero_secreto:
        print('Mi numero es mas bajo')
    
    if estimado == numero_secreto:
        print(f"Felicitaciones {nombre}! Has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"Lo siento, se han agotado los intentos.  El numero secreto era {numero_secreto}")

# Otra manera de resolver el problema

intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: ")

print(f'Bueno {nombre}, he pensado un numero entre 1 y 100\nTienes 8 intentos para adivinar')

while intentos < 8:
    estimado = int(input('Cual es el numero: '))
    intentos = intentos + 1

    if estimado not in range(1,101):
        print('tu numero no se encuentra en el ranfo que va del 1 al 100')
    elif estimado < numero_secreto:
        print('Mi numero es mas alto')
    elif estimado > numero_secreto:
        print('Mi numero es mas bajo')
    else:
        print(f"Felicitaciones {nombre}! Has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"Lo siento, se han agotado los intentos.  El numero secreto era {numero_secreto}")
