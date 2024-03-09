lista = [6,9,4,12,8]
valor = int(input("Ingrese un valor"))

def buscador(lista, valor):
    for i in lista:
        if i == valor:
            print(lista.index(valor))
            break

buscador(lista, valor)