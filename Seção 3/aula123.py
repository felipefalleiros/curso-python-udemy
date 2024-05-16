# Escopo da classe e métodos da classe
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

        # variavel apenas do escopo do init
        variavel = 'variável de dentro do init'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

# print(variavel) será executado na criação do objeto
leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('carne'))
