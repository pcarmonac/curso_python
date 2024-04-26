nombres = ['ana','hugo','valeria']
edades = [65,29,42]
paises = ['lima','madrid','mexico']

combinado = list(zip(nombres,edades,paises))

print(combinado)

for nombre,edad,paises in combinado:
    print(f"{nombre} tiene {edad} años y vive en {paises}")

#Ejercicio 1
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinado = list(zip(paises,capitales))

for paises,capitales in combinado:
    print(f"La Capital de {paises} es {capitales}")

#Ejercicio 3
esp = ['uno','dos','tres','cuatro','cinco']
port = ['um','dois','três','quatro','cinco']
ing = ['one','two','three','four','five']

numeros = list(zip(esp,port,ing))

print(numeros)