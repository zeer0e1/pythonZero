"""
Formatação de string
s - string
d - int
f - float
. <numero de digitos>f
    exemplo
    :.3f
(Caractere) (><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Exe: 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'

print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel:@^10}')
print(f'{223434343:.1f}')

