# Filter e um filtro funcional
# filter(funcao, iteravel)

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

def filtrar_preco(produto):
    return produto['preco'] > 100

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Gera uma lista pegando apenas os dicionarios cujo o preco e maior que 10 utilizando list comprhension
novos_produtos = [p for p in produtos if p['preco'] > 10]
print_iter(novos_produtos)

# Utilizando filter + lamda
novos_produtos2 = filter(lambda p: p['preco'] > 10 ,produtos)
print_iter(novos_produtos2)

# utilizando filter + funcao (filtrar_preco)
novos_produtos2 = filter(filtrar_preco ,produtos)
print_iter(novos_produtos2)