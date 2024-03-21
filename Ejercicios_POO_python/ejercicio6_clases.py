class Familia:
    def __init__(self, padre=str, madre=str, hijos=[]):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos
    
    def __str__(self) -> str:
        return f"Familia de {self.padre}, {self.madre} y sus hijos {self.hijos}"

#Bloque principal
familia = Familia("Gustavo", "Maria", ["Lautaro", "Francisco"])
print(familia)