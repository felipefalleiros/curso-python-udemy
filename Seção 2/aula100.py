# Deep copy uso do modulo copy(), 
# Exercicios
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
print('TABELA ORIGINAL')
print(*produtos, sep= '\n')

# Aumente os precos dos produtos a seguir em 10%
# gere novos_produtos por deep copy (copia profunda)
novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.10)}
    for produto in produtos
]
print('\nAUMENTO DE 10% NOS PRECOS')
print(*novos_produtos, sep= '\n')
print()

# Ordene os produtos por nome decrescente
# Gere produtos_ordenados_por_nome por deep copy

produtos_ordenados_por_nome = [
    {**produto, 'nome': produto['nome']}
    for produto in produtos
]
produtos_ordenados_por_nome = sorted(produtos, key= lambda item: item['nome'], reverse=True)
print('NOMES EM ORDEM DECRESCENTES')
print(*produtos_ordenados_por_nome, sep='\n')
print()

# Ordene os produtos por preco crescente
# Gere produtos_ordenados_por_preco por deep copy

produto_ordenado_por_preco = [
    {**produto, 'preco':produto['preco']}
    for produto in produtos
]
produto_ordenado_por_preco = sorted(produtos, key= lambda item: item['preco'])
print('ORDENADOS POR PRECO CRESCENTE')
print(*produto_ordenado_por_preco, sep='\n')
print()

