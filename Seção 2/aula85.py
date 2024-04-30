# Sem usar list comprehension
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

 # Usando list comprehension       
lista1 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]

print(lista)