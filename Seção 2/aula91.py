# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))
# yield pausa a execucao e espera a chamada do next

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=100000)
for n in gen:
    print(n)