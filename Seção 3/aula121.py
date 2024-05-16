# Métodos em instâncias de classes Pytonh
# Hard coded - É algo que foi escrito diretamente no código
class Carro:
    def __init__(self, nome):
        self.nome = nome
    # Método é uma função dentro da classe
    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()