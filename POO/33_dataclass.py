# Dataclasses - O que são datacalsses ?
# o módulo dataclasses forncece um decorador e funções para criar
# métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário
# Em resumo/. dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int


if __name__ == '__main__':
    p1 = Pessoa('Lucacs', 26)
    print(p1)
