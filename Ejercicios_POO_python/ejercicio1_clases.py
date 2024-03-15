class Persona:
    def inicializar(self, name: str):
        self.nombre = name
    
    def imprimir(self):
        print("Nombre:", self.nombre)
        
#Bloque principal
persona1 = Persona() 
persona1.inicializar("Franco")
persona1.imprimir()

persona2 = Persona()
persona2.inicializar("Lionel")
persona2.imprimir()