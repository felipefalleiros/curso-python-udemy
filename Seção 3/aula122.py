# Entendendo self em classes python
# Self faz referência a própria instância
# Classe - molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias

class Carro:
    def __init__(self, nome):
        self.nome = nome

    # Método é uma função dentro da classe
    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()
Carro.acelerar(fusca)

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()
Carro.acelerar(celta)
