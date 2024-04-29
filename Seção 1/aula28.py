nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome != '' and idade != '':
    print(f'Seu nome é {nome.upper()}')
    print(f'Seu nome invertido é {nome.upper()[::-1]}')
    if (' ' in nome):
        print('Seu nome tem espaço')
    else:
        print('Seu nome não tem espaço')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome.upper()[0]}')
    print(f'A última letra do seu nome é {nome.upper()[-1]}')
else:
    print('Desculpe, você deixou campos vazios!')

