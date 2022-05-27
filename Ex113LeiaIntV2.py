def leiaInt(txt):
    val = 0
    ok = False
    while True:
        try:
            val = int(input(txt))
        except (ValueError, TypeError):
            print('\033[0;31mErro, Digite um nuemro inteiro!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mEntrada de Dados interrompida\033[m')
            return 0
        else:
            return val


def leiaFloat(txt):
    val = 0
    ok = False
    while True:
        try:
            val = float(input(txt))
        except (ValueError, TypeError):
            print('\033[0;31mErro, Digite um nuemro real!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mEntrada de Dados interrompida\033[m')
            return 0
        else:
            return val


n = leiaInt('Digite um numero inteiro: ')
o = leiaFloat('Digite um numero real: ')
print(f'Voce digitou {n}')
print(f'Voce digitou {o}')
