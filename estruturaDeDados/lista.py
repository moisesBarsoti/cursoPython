# Listas - Ela armazena de maneira sequencial qualquer tipo de objeto

frutas = ['Maça', 'Uva', 'Limão']
lista = list("uva")
numeros = list(range(10))
print(frutas)
print(lista)
print(numeros)


# Vetor - Ela é composta somente por uma linha
            # 0     # 1     # 2
frutas2 = ["Banana","Uva","Melão"] 
print(frutas2[2]) # Melão
print(frutas2[0]) # Banana

# Indice negativo
            # -3     # -2     # -1
frutas3 = ["Limão","Uva","Melão"] 
print(frutas2[-2]) # Uva
print(frutas2[-1]) # Melão


# Matriz - Ela é composta por linhas e coluna

matriz = [
    ["a", 3, "b"],
    ["c", 4, "d"],
    ["e", 5, "f"]
]

print(matriz[1][-1]) # d
print(matriz[2][2]) # f


# Iteração - Serve para saber o que tem dentro do elemento que você está selecionando

carros = ["Gol", "GTR", "Porsche"]

for carro in carros:
    print(carro)


# Fatiamento - Ele retorna o que você quer dentro da lista

numbers = [1,2,543,6787,8796,432,64,8,90,]
pares = []

for number in numbers:
    if number % 2 == 0:
       pares.append(number)
       print(number) 


# Outro exemplo de Fatiamento

numbers2 = [1,2,3,4,5,6,7,8,9,10]
pares = [number2 for number2 in numbers2 if number2 % 2 == 0]
print(pares)

numbers3 = [1,2,3,4,5,6,7,8,9,10]
quadrado = [number ** 2 for number in numbers3]
print(quadrado)
