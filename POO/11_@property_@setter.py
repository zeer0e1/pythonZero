# property + @setter  = getter e setter no modo pythonico
# é como o getter
# - para evitar quebrar codigo cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# atributos que começar com um ou dois underlinas nao devem ser usados fora
# da clsse

class Caneta:
  def __init__(self, cor):
    self._cor = cor
    self._cor_tampa = None
  
  @property
  def cor (self):
    print('PROPERTY')
    return self._cor
  
  @cor.setter
  def cor(self,valor):
    self._cor = valor
  
  @property #getter
  def cor_tampa(self):
    return self._cor_tampa
    
  @cor_tampa.setter #setter
  def cor_tampa(self,valor):
    self._cor_tampa = valor
  
caneta = Caneta('Azul')
# getter -> obter valor
print(caneta.cor)
print(caneta.cor_tampa)
caneta.cor_tampa = 'Verde'
print(caneta.cor_tampa)