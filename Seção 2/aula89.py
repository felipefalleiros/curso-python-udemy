# dir lista os nomes dos atributos e metodos disponiveis em um objeto
# hasattr verifica a existencia de um metodo para um objeto
# getattr 
string = 'Luiz'
metodo = 'strip'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)