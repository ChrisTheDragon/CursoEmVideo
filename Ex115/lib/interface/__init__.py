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


def linha(tam = 42):
    return '-'*tam


def cabeçalho(txt, tam=42):
    print(linha())
    print(txt.center(tam))
    print(linha())


def menu(lista):
    c = 1
    cabeçalho('MENU PRINCIPAL')
    for item in lista:
        print(f'\033[1;33m{c}\033[m - \033[1;34m{item}\033[m')
        c += 1
    opc = leiaInt('-> ')
    print(linha())
    return opc