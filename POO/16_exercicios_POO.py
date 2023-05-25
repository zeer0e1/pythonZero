class Carro:
  def __init__(self, nome, motor, fabricante):
    self._nome = nome
    self._motor = motor
    self._fabricante = fabricante
    
  @property
  def nome_carro(self):
    return self._nome
  
  @property
  def nome_fabricante(self):
    return self._fabricante
  
  @nome_fabricante.setter
  def nome_fabricante(self, nome):
    self._fabricante = nome
  
  @property
  def nome_motor(self):
    return self._motor
  
  @nome_motor.setter
  def nome_motor(self, nome):
    self._motor = nome
  
  
class Motor:
  def __init__(self,nome):
    self.nome = nome

class Fabricante:
  def __init__(self,nome):
    self.nome = nome


motor1 = Motor('Opala')
fabricante = Fabricante('WolksWagen')

fusca =  Carro('Fusca',motor1.nome,fabricante.nome)

print(fusca.nome_carro,fusca.nome_fabricante,fusca.nome_motor)


