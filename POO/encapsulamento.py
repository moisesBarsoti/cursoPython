# Encapsulamento ele define o modificador de acesso

class conta:
    def __init__(self, saldo, numDaAgencia):
        self._saldo = saldo
        self.numDaAgencia = numDaAgencia

    def sacar(self, valor):
        self._saldo -= valor
    
    def depositar(self, valor):
        self._saldo += valor



conta1 = conta(100, 23123)
conta1.depositar(100)
print(conta1)
print("Olá Mundo")