def executa(funcao, *args):
    return funcao(*args)


# def soma(x, y):
#     return x + y

print(
    executa(
        lambda x, y: x + y, 2, 3  # Função soma escrita em lambda
    )
)

# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

duplica = executa(
    lambda m: lambda n: n * m, 2    # Função cria multiplicador escrita em lambda (2 é arg da primeira parte da função, o multiplicador)
)

print(duplica(3)) # 3 é arg da segunda parte da função, número a ser multiplicado (n)