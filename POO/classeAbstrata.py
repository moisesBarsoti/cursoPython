class ControleRemoto:
    def __init__(self, nomeDoControle):
        self.nomeDoControle = nomeDoControle
    
    def ligar(self):
        print(f"{self.nomeDoControle} Ligando")    
    
    def desligar(self):
        print(f"{self.nomeDoControle} Desligando")

    def mostrarValores(*objs):
        for obj in objs:
            print(obj)


class ControleTV(ControleRemoto):
    def nomeDoControle(self):
        return f"{self.nomeDoControle}"


controle = ControleTV("Controle Samsung")
controle.ligar()
controle.desligar()
controle.mostrarValores()    