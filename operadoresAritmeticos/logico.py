# Operador E - Somente retorna true se todas as condiçõees forem verdadeiras
saldo = 100
saque = 200
limite = 100

print(saldo >= saque and saque <= limite)

# Operador Ou - Somente retorna true se uma das condições forem verdadeiras
saldo = 100
saque = 200
limite = 100

print(saldo >= saque or saque >= limite)

# Operador de negação - A negação vai mostrar o valor inverso por exemplo

n1 = 1000 > 2000 # false
print(not n1) # true