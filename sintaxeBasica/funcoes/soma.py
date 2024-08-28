# Função de soma
def soma(numeros):
    return sum(numeros)

print(soma([50,50,50]))

def numSucessorNumAntecessor(numeros):
    numerosAntecessor = numeros - 1
    numerosSucessor = numeros + 1
    return print(numerosAntecessor, numerosSucessor)

print(numSucessorNumAntecessor(10))    