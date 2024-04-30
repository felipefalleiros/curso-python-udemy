# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}
# print(produto)
# print(produto.keys())
# print(produto.values())
# print(produto.items())



# dc = {
#     chave: valor.upper()
#     if isinstance(valor, str) else valor
#     for chave, valor
#     in produto.items()
#     if chave != 'categoria'
# }
# print(dc)

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]
dc = {
    chave: valor
    for chave, valor in lista
}

# print(dc)
s1 = {i for i in range(1, 11)}
print(s1)
