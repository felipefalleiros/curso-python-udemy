# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores sao "Syntax Sugar" (Acucar sintatico)

# Funcao decoradora nao retorna um resultado mas sim uma outra funcao que sera executada posteriormente quando for chamada
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

# Faz com que a funcao inverte_string utilize a funcao criar_funcao
@criar_funcao
def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

# Sem a utilizacao do syntax sugar precisariamos utilizar todas as linhas abaixo
# inverte_string_checando_parametro = criar_funcao(inverte_string)
# invertida = inverte_string_checando_parametro('123')
# print(invertida)

# Com o uso do syntax sugar utilizamso apenas
invertida = inverte_string('123')
print(invertida)
