class Triangulo:
    def inicializar(self, ld1: int, ld2: int, ld3: int):
        self.lado1 = ld1
        self.lado2 = ld2
        self.lado3 = ld3

    def imprimir(self):
        ladomayor = max(self.lado1, self.lado2, self.lado3)
        print("Lado mayor:", ladomayor)

    def es_equilatero(self):
        if self.lado1 == self.lado2 and self.lado3:
            print("El triangulo es equilatero")
        else:
            print("El triangulo no es equilatero")
    
#Bloque principal
triangulo1 = Triangulo()
triangulo1.inicializar(2, 2, 2)
triangulo1.imprimir()
triangulo1.es_equilatero()

triangulo2 = Triangulo()
triangulo2.inicializar(2, 7, 9)
triangulo2.imprimir()
triangulo2.es_equilatero()