# Lançando exeções


def divide(n, d):
    try:
        return n / d
    except ZeroDivisionError:
        print('Salvando erro na base de dados')
        raise


print(divide(8, 0))


def deve_ser_inte_ou_float(n1):
    typo_n = type(n1)
    if not isinstance(n1, (float, int)):
        raise TypeError(f'{n1} deve ser do tipo int ou float \n {typo_n.__name__} enviado')


def errozero(d):
    if d == 0:
        raise ZeroDivisionError('Vc está tentando dividir por zero')
    return True


def divide2(n, d):
    deve_ser_inte_ou_float(n)
    deve_ser_inte_ou_float(d)
    errozero(d)
    return n / d


print(divide2(2, '0'))
