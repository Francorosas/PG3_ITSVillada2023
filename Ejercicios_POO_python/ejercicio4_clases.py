class Operacion:
    def __init__(self):
        self.numero1 = int(input("Ingresar primer valor: "))
        self.numero2 = int(input("Ingresar primer valor: "))

    def suma(self):
        suma = self.numero1 + self.numero2
        print("Resultado de la suma:", suma)
    
    def resta(self):
        resta = self.numero1 - self.numero2
        print("Resultado de la resta:", resta)

    def multiplicacion(self):
        multiplicacion = self.numero1 * self.numero2
        print("Resultado de la multiplicacion:", multiplicacion)

    def division(self):
        division = self.numero1 / self.numero2
        print("Resultado de la division:", division)

#Bloque principal
operacion = Operacion()
operacion.suma()
operacion.resta()
operacion.multiplicacion()
operacion.division()
