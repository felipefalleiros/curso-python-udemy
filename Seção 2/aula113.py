# reduce - faz a reducao de um iteravel em um valor
# reduce(funcao, iteravel, valor inicial)
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
def funcao_do_reduce(acumulador, produto):
    print(acumulador)
    print(produto)
    return acumulador + produto['preco']

#sem utilizar reduce
total = 0
for p in produtos:
    total += p['preco']
print(f'{total:.2f}')

print()
# utilizando reduce + funcao
total = reduce(
    funcao_do_reduce, produtos, 0
)
print(f'Total e {total:.2f}')
print()
#utilizando reduce + lambda
total = reduce(lambda ac, p: ac + p['preco'], produtos, 0)
print(f'Total e {total:.2f}')




