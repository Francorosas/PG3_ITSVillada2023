vocales = ("a", "e", "i", "o", "u")
frase = input("Ingrese una frase: ").lower()
def tienevocales(frase, vocales):
    contador = 0
    for i in frase:
        if i in vocales:
            contador += 1
    return contador
            
print("Su frase/palabra contiene", tienevocales(frase,vocales), "vocal/es")
