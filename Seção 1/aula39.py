nome = 'Felipe'
tamanho_nome = len(nome)

cont = 0
novo_nome = ''
while cont < tamanho_nome:
    letra = nome[cont]
    novo_nome += f'*{letra}'
    cont += 1
print(novo_nome)