# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
  def __init__(self,nome):
    self.nome = nome
    self.enderecos = []
    
  def inserir_enderecos(self, rua, numero):
    self.enderecos.append(Endereco(rua, numero))
  
  def listar_enderecos(self):
    for endereco in self.enderecos:
      print(endereco.rua)
  
  def __del__(self):
    print('APAGANDO', self.nome)
  
  
class Endereco:
  def __init__(self,rua,numero):
    self.rua = rua
    self.numero = numero

  def __del__(self):
    print('APAGANDO', self.rua, self.numero)
    
cliente1 = Cliente('Maria')
cliente1.inserir_enderecos('av brasil', 54)
cliente1.inserir_enderecos('Rua b',45)

print(cliente1.enderecos)
cliente1.listar_enderecos()

del cliente1

print('######AQUI TERMINA MEU CÓDIGO')

