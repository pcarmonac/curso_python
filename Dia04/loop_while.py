# monedas = 5

# while monedas > 0:
#     print(f"Tengo {monedas} monedas")
#     monedas = monedas - 1
# else:
#     print("no tengo mas dinero")

# respuesta = 's'

# while respuesta == 's':
#     respuesta = input("quieres seguir? (s/n)")
# else:
#     print("gracias")

# nombre = input("Tu nombre: ")

# for letra in nombre:
#     if letra == 'r':
#         break
#     print(letra)

# nombre = input("Tu nombre: ")

# for letra in nombre:
#     if letra == 'r':
#         continue
#     print(letra)

# EJERCICIOS

# numero = 10

# while numero > -1:
#     print (numero)
#     numero = numero - 1

# Práctica Loop While 2
# Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos) con las siguientes condiciones adicionales:

# - Si el número es divisible por 5, mostrar dicho número en pantalla (¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)

# - Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla (no te olvides de seguir restando para que el programa no corra infinitamente).

numero = 50

while numero > -1:
    if numero % 5