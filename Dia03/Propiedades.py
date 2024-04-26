# esto manda error ya que los str son inmutables
# nombre = "Carina"
# nombre[0] = "K"

# print (nombre)

n1 = "Kari"
n2 = "na"

print(n1 + n2) # concatenar

print(n1 * 10) # multiplicar

poema = """mil pequeños peces blancos
com si hirviera
el color del agua"""

print (poema) # saltos de linea usando comillas dobles

print("agua" in poema) # Booleano si la palabra esta en el str
print("sol" in poema) # Booleano False
print("sol" not in poema) # booleano de doble negacion que entrega True

print(len(poema))
