"""
Imprecisão de ponto flutuante
"""
import decimal

n1 = 0.1
n2 = 0.7
n3 = n1 + n2 
print(n3)

# Primeira maneira
print(f'{n3:.2f}')

# Segunda maneira
print(round(n3,2))

# Terceira forma
print(decimal.Decimal(n3))