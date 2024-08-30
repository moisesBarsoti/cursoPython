contatos = {
    "teste2.teste@gmail.com": {"nome": "Moises", "idade": 19},
    "teste3.teste@gmail.com": {"nome": "Moises", "idade": 19},
    "teste4.teste@gmail.com": {"nome": "Moises", "idade": 19}
}

# Clear - Ele apaga todos os valores do dicionário
# contatos.clear()

# Copy - Ele faz uma cópia
copia = contatos.copy()
print(copia)

# Fromkeys - Ele cria valor para você
print(dict.fromkeys(["nome","Idade"])) # {'nome': None, 'Idade': None}
print(dict.fromkeys(["nome","Idade"],"vazio")) # {'nome': 'vazio', 'Idade': 'vazio'}

# Get - Ele pega as chaves
pessoa = {
    "pessoa1": {"Nome":"Moises","Idade":19},
    "pessoa2": {"Nome":"Luciana","Idade":40},
    "pessoa3": {"Nome":"Laryssa","Idade":14},
}
print(pessoa.get("pessoa1")) # {'Nome': 'Moises', 'Idade': 19}
print(pessoa.get("pessoa2")) # {'Nome': 'Luciana', 'Idade': 40}
print(pessoa.get("pessoa3")) # {'Nome': 'Laryssa', 'Idade': 14}

# Items - ELe retorna uma tupla
pessoa2 = {
    "pessoa1": {"Nome":"Moises","Idade":19},
    "pessoa2": {"Nome":"Luciana","Idade":40},
    "pessoa3": {"Nome":"Laryssa","Idade":14},
}
print(pessoa2.items()) # dict_items([('pessoa1', {'Nome': 'Moises', 'Idade': 19}), ('pessoa2', {'Nome': 'Luciana', 'Idade': 40}), ('pessoa3', {'Nome': 'Laryssa', 'Idade': 14})])

# Keys - ELe retorna somente as chaves
pessoa3 = {
    "pessoa1": {"Nome":"Moises","Idade":19},
    "pessoa2": {"Nome":"Luciana","Idade":40},
    "pessoa3": {"Nome":"Laryssa","Idade":14},
}
print(pessoa3.keys()) # dict_keys(['pessoa1', 'pessoa2', 'pessoa3'])

# POP - Ele remove o elemento
pessoa4 = {
    "pessoa1": {"Nome":"Moises","Idade":19},
    "pessoa2": {"Nome":"Luciana","Idade":40},
    "pessoa3": {"Nome":"Laryssa","Idade":14},
}
print(pessoa4.pop("pessoa1")) # dict_keys(['pessoa1', 'pessoa2', 'pessoa3'])