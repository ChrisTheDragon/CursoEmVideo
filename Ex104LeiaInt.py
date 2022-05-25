def leiaInt(txt):
    val = 0
    ok = False
    while True:
        num = str(input(txt))
        if num.isnumeric():
            val = int(num)
            ok = True
        else:
            print('\033[0;31mErro, Digite um nuemro inteiro!\033[m')
        if ok:
            break
    return val


n = leiaInt('Digite um numero: ')
print(f'Voce digitou {n}')
