def inverter_dicionario(dicionario):
    return {valor: chave for chave, valor in dicionario.items()}

# Exemplo de uso:
dicionario = {'a': 1, 'b': 2, 'c': 3}
print(inverter_dicionario(dicionario))
