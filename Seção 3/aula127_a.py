# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_ARQUIVO = 'aula127.txt'
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

p1 = Pessoa('João', 33)
p2 = Pessoa('Maria', 29)
p3 = Pessoa('Pedro', 19)
p4 = Pessoa('Sarah', 15)

pessoas = [vars(p1),vars(p2), vars(p3), vars(p4)]

# envolver numa função para adiar a execução
def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w' , encoding='utf-8') as arquivo:
        print('FAZENDO DUMP')
        json.dump(pessoas, arquivo, ensure_ascii=False, indent=2)
