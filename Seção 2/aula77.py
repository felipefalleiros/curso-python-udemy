# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',

    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',

    },
    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',

    }
]

acertos = 0
for questao in perguntas:   
    print(f'Pergunta: {questao['Pergunta']}')
    print()
    print(f'Opções:')
    lista_alternativas = questao['Opções']   
    for valores in lista_alternativas:
        i = lista_alternativas.index(valores)
        print(f'{i})  {valores}')


    resp = input('Escolha uma opção: ')
    resposta_correta = questao['Resposta']   
    if int(resp) == lista_alternativas.index(resposta_correta) :
        print('ACERTOU')
        acertos += 1
    else:
        print('ERROU')
    print()

print (f'Você acertou {acertos} \nde {len(perguntas)} perguntas.')
    
