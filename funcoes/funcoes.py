# Funções - É um bloco de código que reutilizamos em outras partes do código
def exibirMensagem():
     return print("Olá mundo")


def exibirName(name):
    return print(f"O meu nome é: {name}")


def exibirName2(name="Anônimo"):
    return print(f"O meu nome é: {name}")


print(exibirMensagem())    
print(exibirName("Moisés"))    
print(exibirName2())    