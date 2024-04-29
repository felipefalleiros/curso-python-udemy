while True:
    n1 = input('Digite o primeiro número: ')
    n2 = input('Digite o segundo número: ')
    operador = input('Qual operação deseja realizar? (+, -, *, /) ')
    
    n_valido = None

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        n_valido = True     # Caso os números sejam validos avar n_validos será True 

    except:
        n_valido = None

    # checagem dos números
    # se for True, o continue jogara o programa para o inicio do laço
    if n_valido is None:
        print('Um ou ambos os números são inválidos!')
        continue
    
    # checagem de operadores
    op_permit = '+-*/'
    #se o operador digitado não estiver entre os permitidos, o continue jogara o programa para o inicio do laço
    if operador not in op_permit:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')

    if operador == '+':
        calc = n1_float + n2_float
        print(calc)
    elif operador == '-':
        calc = n1_float - n2_float
        print(calc)
    elif operador == '*':
        calc = n1_float * n2_float
        print(f'{calc:.1f}')
    elif operador == '/':
        calc = n1_float / n2_float
        print(f'{calc:.1f}')
    else:
        print('Por favor, digite um operador válido!')
    
    resp = input('Deseja sair? [S/N]')
    resp = resp.lower()                 # transforma resp em minusculo
    resp = resp.startswith('s')         # resp começa com 's'? retorna bool
    if resp is True:
        break

