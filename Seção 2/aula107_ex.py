# Considerando duas listas de int ou floats
# Some os valores dnas listas retornando uma nova lista com os valores somados:

# Se uma lista for maior que a outra, a soma so vai considerar o tamanho da menor.

# Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

# Resultado:
# lista_soma = [2, 4, 6, 8]

lista_soma = []

# for n in range(len(lista_b)):
#    lista_soma.append(lista_a[n] + lista_b[n])

# print(lista_soma)

#Solucao utilizando recursos do python
# for i, n in enumerate(lista_b):
#    lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# utilizando list comprehension + zip
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)
