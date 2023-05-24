# Emcapsulamento (modificadores de acesso: public, protect, private)
# Python NÃO TEM modificadores de acesso
# mas podemos seguir as seguintes covenções:
"""
  (sem underline) = public
            pode ser usado em qualquer lugar
  
- (um underline) = protected
            não DEVE ser usado fora da classe ou das subsclasses
__(dois underlines) = private
            "name mangling" (desfiguração de nomes) em Python
            só DEVE ser usado na classe em que foi declarado
"""

class Foo:
  def __init__(self):
    ...