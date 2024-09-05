class Veiculo:
    def  __init__(self, marca, cor, placa, numeroDeRodas):
        self.marca = marca
        self.cor = cor
        self.placa = placa
        self.numeroDeRodas = numeroDeRodas

    def ligarMotor(self):
        print(f"{self.marca} Ligando motor")    

class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    pass


moto = Motocicleta("Motocicleta","Preta", "abc-1234", 2)
moto.ligarMotor()

carro = Carro("Gtr","Preto", "abc-1234", 4)
carro.ligarMotor()

caminhao = Caminhao("Caminhao","Preto", "abc-1234", 4)
caminhao.ligarMotor()