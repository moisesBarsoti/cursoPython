class Cliente:
    def __init__(self, nome, saldo, idade):
        self.nome = nome
        self.saldo = saldo
        self.idade = idade

    def sacar(self, valor):
        
        if self.saldo <= valor:
            print(f"Você não pode sacar este valor de R${valor}")
        else:
            self.saldo -= valor 

    
    def depositar(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"Nome: {self.nome} Idade: {self.idade} Saldo: {self.saldo}"    

cliente = Cliente("Moises", 100, 19)             
cliente.depositar(100)
cliente.sacar(300)
print(cliente)