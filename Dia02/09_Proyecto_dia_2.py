nombre = input("Ingrese su nombre: ")
ventas = input("Ingrese el monto de sus ventas: ")

ventas_flo = float(ventas)

comision = round((ventas_flo * 13)/100,2)

print(f"La comision de {nombre} segun sus ventas {ventas} es de {comision}")