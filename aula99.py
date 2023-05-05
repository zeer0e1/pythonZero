from sys import  path

from aula99_package.modulo import soma_modulo

print(__name__)
print(*path, sep='\n')

print(soma_modulo(2, 3))

