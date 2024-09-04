class Bicicleta343534:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Buzinando...")    
    
    def parar(self):
        print("Parando...")    
        print("Bicicleta parou")    
    
    def correr(self):
        print("Bicicleta está correndo...")    

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"    

bicicleta1 = Bicicleta343534('Branco','caloi',2020,300)        
print(bicicleta1.__str__())