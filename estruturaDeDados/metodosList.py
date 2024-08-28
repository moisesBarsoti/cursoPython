# Append - Ele coloca o valor que você deseja na frente do valor
frutas = ['Maça', 'Uva', 'Morango']
frutas.append("Amora")
print(frutas) # ['Maça', 'Uva', 'Morango', 'Amora']

# Clear - Ele limpa a sua lista
lista = ['a','b','c']
lista.clear()
lista.append('d')
print(lista) # ['d']

# Copy - Ele faz uma copia da sua lista
lista1 = ['a','b','c']
lista2 = lista1.copy()

print(id(lista1), id(lista2))

# Count - Ele mostra quantas vezes o elemento aparece na lista
carros = ['GTR','Gol',]
print(carros.count("GTR")) # 1

# Extends - Ele faz o ajuntamento de uma lista com outra
linguagens = ['Python', 'JS']
linguagens.extend(['Java', 'C#'])
print(linguagens) #['Python', 'JS', 'Java', 'C#']

# POP - Remove o ultimo elemento da lista através do indice
linguagens2 = ['Java','C#','Typescript','Python']
linguagens2.pop()
print(linguagens2) # ['Java', 'C#', 'Typescript']

# Remove - Remove o elemento através do objeto
linguagens3 = ['Java','C#','Typescript','Python']
linguagens3.remove('Java')
print(linguagens3) # ['C#', 'Typescript', 'Python']

# Reverse - Ele inverte a lista
linguagens4 = ['Java','C#','Typescript','Python']
linguagens4.reverse()
print(linguagens4)

# Sort - Ele ordena em ordem alfabetica
linguagens5 = ['Java', 'Python', 'JS', 'C']
linguagens5.sort()
linguagens5.sort(reverse=True) # Ele coloca em ordem alfabetica de forma invertida
linguagens5.sort(key=lambda x: len(x)) # Ele pega por tamanho da palavra
print(linguagens5) # ['C', 'JS', 'Java', 'Python']