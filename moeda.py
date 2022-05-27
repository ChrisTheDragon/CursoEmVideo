def dobro(valor=0, form=False):
    return valor * 2 if not form else moeda(valor * 2)


def metade(valor, form=False):
    return valor / 2 if not form else moeda(valor / 2)


def aumentar(valor, p, form=False):
    return moeda(valor + (valor * p / 100)) if form else valor + (valor * p / 100)


def diminuir(valor, p, form=False):
    return moeda(valor - (valor * p / 100)) if form else valor - (valor * p / 100)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>.2f}'.replace('.', ',')


def resumo(valor, a, b):
    print(f'-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print(f'-' * 30)
    print(f'Preço analizado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'Aumentando {a}%: \t{aumentar(valor, a, True):^10}')
    print(f'Diminuindo {b}%: \t{diminuir(valor, b, True):^10}')
    print(f'-' * 30)
