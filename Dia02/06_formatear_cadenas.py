x = 10
y = 5

print("Mis numeros son " + str(x) + " y " + str(y)) # manera tradicional de mostrar INT en un print de STR, transformando las variables, haciendo una concatenacion

print("Mis numeros son {} y {}".format(x,y)) # utilizando instruccion format

print("La suma de {} y {} es igual a {}".format(x,y,x+y)) # resuelto utilizando formateando cadenas, sin hacer concatenaciones.

color = "rojo"
matricula = 54321

print(f"El auto es {color} y su matricula es {matricula}") # usando cadenas literales