# Generetor expressions, iterables e iterators em python
iterable = ['Eu' , 'Tenho', '__iter__']
iterator = iterable.__iter__() # tem __iter__ e __next__

lista = [n for n in range(10)]
generator = (n for n in range(10))
print(generator)

# iterator trabalha com iteravel que trabalha com as classes iter e next
# generator e uma funcao que pausa e so passa o proximo valor se a funcao next for chamada