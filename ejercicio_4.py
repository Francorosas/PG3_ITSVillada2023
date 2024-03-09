lista = []
cant = int(input("Cuantos numero desea agregar a la lista: "))
for i in range (cant):
    valor = int(input("INGRESE EL NUMERO: "))
    lista.append(valor)
lista.sort()
print("La lista ordenada seria la siguiente: ", lista)