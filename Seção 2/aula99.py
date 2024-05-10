# from sys import path

# # Diferentes formas de importar modulo.py
# import aula99_package.modulo
# from aula99_package import modulo

# # Vai importar somente oq estiver dentro do __all__ no modulo.py
# from aula99_package.modulo import *

# from aula99_package.modulo import soma_do_modulo

# # print(*path, sep='\n')
# print(soma_do_modulo(1, 2)) # from aula99_package.modulo import soma_do_modulo
# print(aula99_package.modulo.soma_do_modulo(1, 2)) # import aula99_package.modulo
# print(modulo.soma_do_modulo(1, 2)) #from aula99_package import modulo
# print(variavel) #from aula99_package.modulo import *
# print(nova_variavel) #from aula99_package.modulo import *

# from aula99_package.modulo import soma_do_modulo, fala_oi

# fala_oi()

from aula99_package import soma_do_modulo, falar_oi
print(soma_do_modulo(2, 4))
falar_oi()