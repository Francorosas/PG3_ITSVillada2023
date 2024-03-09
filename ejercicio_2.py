def aniobisiesto(anio):
    if (anio % 4 == 0 or anio % 400 == 0 and anio % 100 != 0):
        print("es bisiesto")
    else:
        print("no es bisiesto")

        
anio = int(input("Ingrese un anio: "))
aniobisiesto(anio)