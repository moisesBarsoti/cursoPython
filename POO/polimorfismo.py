# Polimorfismo - É o mesmo metodo com comportamento diferente

class Passaro:
    def __init__(self, passaro, voar="voando"):
        self.passaro = passaro
        self.voar = voar

    def __str__(self) -> str:
        return f"Passaro: {self.passaro}\n asas: {self.voar}"    

class Pardal(Passaro):
    def voar(self):
        return super().voar()
    
passaro = Pardal("Pardal")
print(passaro)    