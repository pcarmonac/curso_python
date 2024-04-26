# proyecto dia 03
lista_letra = [0,0,0]

# ingreso de informacion
texto_usr = input("Favor ingrese texto: ")
letra_1 = input("Favor ingrese letra 1: ")
letra_2 = input("Favor ingrese letra 2: ")
letra_3 = input("Favor ingrese letra 3: ")

# conversion a minusculas
texto_usr = texto_usr.lower()
letra_1 = letra_1.lower()
letra_2 = letra_2.lower()
letra_3 = letra_3.lower()

# traspasar texto y letras a lista
lista_letra[0] = letra_1
lista_letra[1] = letra_2
lista_letra[2] = letra_3
lista_texto = texto_usr.split()

# analisis

# 01 cuantas veces aparece cada letra
res1 = texto_usr.find(letra_1)
res2 = texto_usr.find(letra_2)
res3 = texto_usr.find(letra_3)

print(f"\nLa letra {letra_1} aparece en el texto {res1} veces")
print(f"La letra {letra_2} aparece en el texto {res2} veces")
print(f"La letra {letra_3} aparece en el texto {res3} veces")

# cuantas palabras en texto
largo = len(lista_texto)
print(f"\nLa cantidad de palabras del texto es {largo}")

# primera y ultima letra
cap1 = texto_usr[0]
largo = len(texto_usr) - 1
cap2 = texto_usr[largo]

print(f"\nLa primera letra del texto es {cap1} y la ultima {cap2}")

# mostrar texto invertido
lista_texto.reverse()

print(f"\nEl texto invertido seria\n{lista_texto}")

# buscando la palabra Python
print("\nBUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto_usr
dic = {True:"sí", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto\n")
 