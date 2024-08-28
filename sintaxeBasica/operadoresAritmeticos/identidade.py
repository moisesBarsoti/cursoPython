# Identidade eles são utilizados para comparar se os dois objetos ocupam o mesmo espaço na memória

# Is - Ele siginifica o mesmo que "é" ou seja ele verifica se é igual
curso = "Curso Phyton"
nomeCurso = curso
print(curso is nomeCurso) # True

saldo = 100
limite = 100
print(saldo is limite) # false