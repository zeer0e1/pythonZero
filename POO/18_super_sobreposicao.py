# super() é a super classe na sub classe
# Classe principal (Pessoa)
"""
  -> super class, base class, parent class
Classes filhas (Cliente)
  -> sub class, child class, derived class
"""

# class MinhaStr(str):
#   def upper(self):
#     print('CHAMOU UPPER')
#     return  super().upper()

# string = MinhaStr('Lucas')
# print(string.upper())

class A:
  atributo_a = 'valor a'
  def metodo(self):
    print('A')

class B(A):
  atributo_b = 'valor b'
  def metodo(self):
    print('B')
    
class C(B):
  atributo_c = 'valor c'
  
  
  def metodo(self):
    super().metodo()
    print('C')

c = C()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()