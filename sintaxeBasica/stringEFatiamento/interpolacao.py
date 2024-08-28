name = "Moisés"
age = 19
pi = 3.144235

# %s = String
# %d = número inteiro

print("Nome: %s idade %d" %(name, age)) # Metodo antigo

print("Nome: {} idade {}".format(name, age)) # Metodo antigo

print(f"Nome: {name} idade {age}") # Metodo novo

print(f"O valor de pi é: {pi: .5f}")