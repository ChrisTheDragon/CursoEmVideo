from random import randint


def sorteio(lst):
    for i in range(0, 5):
        lst.append(randint(0, 10))
    print(f'Os numeros sorteados foram: {lst}')


def somaPar(lst):
    s = 0
    for i in range(len(lst)):
        if lst[i] %2 == 0:
            s += lst[i]
    print(f'A soma dos numeros pares de {lst} é {s}')


num = []
sorteio(num)
somaPar(num)