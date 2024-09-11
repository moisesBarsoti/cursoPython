class Conta:
    def __init__(
            self, 
            saldo,
            numero,
            agencia,
            cliente,
            historico
            ):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    def saldo(self):
        return f"{self.saldo}"
    
    def novaConta(self, cliente, numero):
        self.cliente = cliente    
        self.numero = numero    

    def sacar(self, valor):
        if(self.saldo < valor):
            print(f"Você não pode sacar este valor R${valor}")
        else:    
            self.saldo -= valor    

    def depositar(self, valor):
        self.saldo += valor   

class contaCorrente(Conta):
    def limite(self,):
        self.limite = 3