# Exercicio - Unir lsitas
# Crie uma funcao zipper
# O trabalho dessa fncao sera unir duas listas na ordem
# use todos os valores da menor lista
# ex:
# ['Salvador', 'Ubatuba', 'Belo horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado:
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo horizonte', 'MG'

def zipper(lista1, lista2):
    intervalo = min(len(lista1), len(lista2)) #retorna o menor valor entre os argumentos passados
    return[
        (lista1[i],lista2[i]) for i in range(intervalo)
    ]

l1 = ['Salvador', 'Ubatuba', 'Belo horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(l1,l2))

# utilizando uma funcao do python
print(list(zip(l1,l2)))

# usando os valores da lista maios
from itertools import zip_longest
print(list(zip_longest(l1,l2)))

