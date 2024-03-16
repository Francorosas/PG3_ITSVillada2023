class Persona:
    def __init__(self):
        self.nombre = str(input("Ingresar nombre: "))
        self.edad = int(input("Ingresar edad: "))
    
    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
    
#Bloque principal
persona = Persona()
persona.imprimir()

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = int(input("Ingresar sueldo: "))
    
    def imprimir(self):
        if self.sueldo > 3000:
            print("Usted debe pagar impuestos")
        else:
            print("Usted no debe pagar impuestos")

#Bloque empleado
empleado = Empleado()
empleado.imprimir()