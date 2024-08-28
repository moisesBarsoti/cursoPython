# String - Armazaena um texto

curso = "PytHoN"

# Upper - deixa todas as letras maiúsculas
print(curso.upper(), "1") # PYTHON

# Lower - deixa todas as letras minúsculas
print(curso.lower(), "2") # python

# Title - deixa todas as letras minúsculas exceto a primeira letra
print(curso.title(), "3") # Python


# Eliminando espaços em branco

curso2 = " Phyton "

# Strip - Remove todos os espaços em branco tanto da esquerda quanto da direita
print(curso2.strip(), "4") # "Python"

# Lstrip - Remove todos os espaços da esquerda
print(curso2.strip(), "5") # "Python "

# Rstrip - Remove todos os espaços da direita
print(curso2.strip(), "6") # " Python"


# Junções e Centralização

curso3 = "Phyton"

# Center - Ele centraliza o elemento no meio
print(curso3.center(9, "#"), "7")

# Join - Ele faz uma iteração e ele adiciona o que você quer
print(".".join(curso3), "8")