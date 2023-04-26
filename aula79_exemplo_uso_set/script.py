# Exemplo de uso
letras = set()

while True:
  letra = input('Digite ')
  letras.add(letra.lower())

  if 'l' in letras:
    print('Ok')
    break

  print(letras)