mi_texto = "Esta es una prueba"
resultado = mi_texto[0]

print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto[9]

print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto[-4]

print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto.index("n") # posicion de la letra n, busca de izquiera a derecha y se detiene donde encuentra la primera

print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto.index("prueba") # sensible a mayusculas

print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a",5,11) # en este caso busca la a desde la posicion 5 a la 11, OJO que la posicion 11 no es inclusiva por lo que busca hasta la 10

print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto.rindex("a") # rindex busca de derecha a izquierda

print(resultado)
