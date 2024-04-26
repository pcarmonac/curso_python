texto = "ABCDEFGHIJKLM"
fragmento = texto[2]

print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5] # en este caso fragmenta y corta de la posicion 2 a la 5, pero sin incluir las posicion 5

print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:] # fragmenta de la posicion 2 hasta el final

print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[:5] # fragmenta desde el inicio hasta la posicion 5

print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10:2] # el primer factor indica donde inicia, el segundo donde termina y el tercero cada cuantos caracteres se salta para fragmentar

print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[::2] # al dejar los dos primeros indices en 0 va a tomar todo el string pero saltando de 2 en 2 fragmentando

print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[::-1] # al poner el tercer indice negativo (-1) toma todas las letras pero desde atras a adelante

print(fragmento)
