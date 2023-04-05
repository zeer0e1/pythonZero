print("JOGO PALAVRA SECRETA")
print('Tente advinhar qual a palavra secreta em menos tentativas possíveis...')

palavra_secreta = 'Lucas'
palavra_tamanho: list[str] = list(len(palavra_secreta) * '*')
nova_string = ''
qtd_tentativas = 0
print(type(palavra_tamanho))
while True:
    print(f'A palavra secreta tem {len(palavra_secreta)} letras')
    letra_digitada = input('Digite uma letra: ')

    if letra_digitada in palavra_secreta:
        index_palavra_digitada = (palavra_secreta.index(letra_digitada))
        palavra_tamanho[index_palavra_digitada] = letra_digitada
        mapped = map(str, palavra_tamanho)
        nova_string = ' '.join(mapped)
    print(nova_string)

    qtd_tentativas += 1

    if '*' not in palavra_tamanho:
        print(f'Parabéns você acertou a palavra em {qtd_tentativas} vezes')
        break
