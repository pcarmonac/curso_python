texto = "Este es el texto de Federico"
resultado = texto.upper() # cambia el texto todo a mayuscula

print(resultado)

texto = "Este es el texto de Federico"
resultado = texto[2].upper() # aca imprime el indice numero 2 en mayuscula

print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.lower() # cambia los caracteres a minusculas

print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.split() # crea una lista y guarda ahi cada palabra del string por separado, tomando como separadores los espacios vacios

print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.split("t") # en este caso los cortes se realizan tomando la t como separador

print(resultado)

a = "aprender"
b = "python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])

print(e)

texto = "Este es el texto de Federico"
resultado = texto.find("s") # cuando find no encuentra el caracter en el texto envia error -1

print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.replace("Federico","Todos") # reemplaza el texto inicial por el segundo

print(resultado)

# pregunta de metodo de string
lista_palabras = ["La","legibilidad","cuenta."]
a = lista_palabras[0]
b = lista_palabras[1]
c = lista_palabras[2]

e = " ".join([a,b,c])
print(e)
