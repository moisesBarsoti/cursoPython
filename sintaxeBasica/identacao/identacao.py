def sacar(valor):
    saldo = 500

    if saldo >= valor:
        saldo -= valor
        print("Valor sacado é de:", saldo)

def depositar(valor):
    saldo = 500
    saldo += valor
    print("O seu saldo é:", saldo)

depositar(100)
sacar(100)        