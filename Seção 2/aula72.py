'''
Exercícios com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável

Crie uma função que fala se o número é par ou ímpar
Retorne se o número é par ou ímpar
'''

def multiplica(*args):
    resultado = 1
    for num in args:
        resultado *= num
    print(resultado)
    return resultado
    

def par_impar(n):
    print('Par') if n%2 == 0 else print('Impar')

resultado = multiplica(2,2,2)
par_impar(resultado)



