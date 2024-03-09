def escapicua(palabra):
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False
    
palabra = input("Ingrese una palabra: ")
print(escapicua(palabra))