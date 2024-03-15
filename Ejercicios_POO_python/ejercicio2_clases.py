class Alumno:
    def inicializar(self, name: str, calificacion: int):
        self.nombre = name
        self.nota = calificacion
    
    def imprimir(self):
        print("Alumno:", self.nombre)
        print("Nota:", self.nota)
        if self.nota >= 4:
            print("Estado: Regular")
        else:
            print("Estado: Libre")

#Bloque Principal
alumno1 = Alumno()
alumno1.inicializar("Franco", 8)
alumno1.imprimir()

alumno2 = Alumno()
alumno2.inicializar("Juan", 2)
alumno2.imprimir()
