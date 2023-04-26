# Set - Conjuntos em python

s1 = set() # vazio
s1 = {'Lucas',1,2,3,4} # Com dados

# Muito eficientes para remover valores duplicados de iteráveis

s2 = {1,2,3,4,4,5,6,7,8}
print(s2)

# Metodos uteis
s3 = set()

s3.add(10)
s3.add('Lucas')
s3.update(('Freitas',1))
print(s3)

# Eliminar um valor
s3.discard('Lucas')

s4 = {1,2,3}
s5 = {2,3,4}
s6 = s4 | s5 # uni os dois sets removendo os duplicados
s6 = s4 & s5 # tras somente os valores existentes nos dois sets
s6 = s4 - s5 # tras somente o valor inexistente no set da direita
s6 = s4 ^ s5 # tras somente o valor unico em ambos os sets
