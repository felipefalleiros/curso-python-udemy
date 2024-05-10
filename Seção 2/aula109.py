# Combinations, Permutations, e Product - Itertools
# Combinacao - Ordem nao importa - iteravel + tamanho do grupo
# Permutacao - Ordem importa
# Produto - Ordem importa e repete valores unicos
from itertools import combinations, permutations , product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'Joao', 'Joana', 'Luiz', 'Leticia'
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unissex'],
    ['algodao', 'poliester'],
]

print_iter(combinations(pessoas,2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))

