"""
Listas dentro de listas e seus indices
"""

salas = [
  ['Maria', 'Helena'],
  ['Elaine',],
  ['Lucas','Fretas','Eduarda']
]


for sala in salas:
  for item in sala:
      print(item)