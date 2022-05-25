c = ['\033[m',
     '\033[0;30;47m',
     '\033[0;30;41m',
     '\033[36m',
     '\033[0;30;45m']


def ajuda(com):
    lin(f'Acessando o Manual do {com}', 3)
    print(c[4], end='')
    help(com)
    print(c[0], end='')


def lin(txt, cor=0):
    print(c[cor], end='')
    print('~' * len(txt))
    print(f'{txt:^}')
    print('~' * len(txt))
    print(c[0], end='')


comando = ''
while True:
    lin('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou Biblioteca => '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
lin('ATÉ LOGO', 2)
