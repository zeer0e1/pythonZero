# Emcapsulamento (modificadores de acesso: public, protect, private)
# Python NÃO TEM modificadores de acesso
# mas podemos seguir as seguintes covenções:
"""
  (sem underline) = public
            pode ser usado em qualquer lugar
  
- (um underline) = protected
            SÓ DEVE ser usado fora da classe ou das subsclasses
            
__(dois underlines) = private
            "name mangling" (desfiguração de nomes) em Python
            SÓ DEVE ser usado na classe em que foi declarado
"""

from functools import partial

class Foo:
  def __init__(self):
    self.public = 'Isso é publico'
    self._protect = 'isso é protegido'
    self.__private = 'Isso é privado'
    
  def metodo_publico(self):
    return 'metodo_publico'
  
  def _metodo_protegido(self):
    return 'metodo protegido'
  
  def __metodo_privado(self):
    return 'metodo privado'
  
  
f = Foo()
print(f.public)
print(f.metodo_publico)