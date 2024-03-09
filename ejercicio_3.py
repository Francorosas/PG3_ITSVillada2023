alto = int(input("Ingresar alto de un rectangulo: "))
ancho = int(input("Ingresar ancho de un rectangulo: "))
caracter = str(input("Ingrese un caracter: "))

for i in range (alto):
    for j in range (ancho):
        print(caracter, end=" ")
    print()
    