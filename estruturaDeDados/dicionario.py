# Dicionario - Um dicionário é um conjunto não-ordenado de pares, chaves:valor
pessoa = {"nome": "Moisés", "idade": 19}

# Outra forma de criar
pessoa2 = dict(nome = "Moisés", idade = 19)

# Caso queira adicionar mais um elemento
pessoa["tel"] = "11-1010-1010" 

print(pessoa)
print(pessoa2)

# Para poder acessar o valor
print(pessoa["nome"])

# Fazer iteração
contatos = {
    "teste2.teste@gmail.com": {"nome": "Moises", "idade": 19},
    "teste3.teste@gmail.com": {"nome": "Moises", "idade": 19},
    "teste4.teste@gmail.com": {"nome": "Moises", "idade": 19}
}

for chaves in contatos:
    print(chaves, pessoa)