from time import sleep


def lin():
    print('')
    print('=-' * 35)


def contagem(ini, fim, pas):
    c = 0
    lin()
    if pas < 0:
        pas *= -1
    if pas == 0:
        pas = 1

    print(f'Contagem de {ini} ate {fim} de {pas} em {pas}: ')
    if ini < fim:
        c = ini
        while c <= fim:
            print(f'[{c}]', end='')
            sleep(0.25)
            c += pas
    else:
        c = ini
        while c >= fim:
            print(f'[{c}]', end='')
            sleep(0.25)
            c -= pas


lin()
print('Contagem de 1 ate 10 de 1 em 1')
for i in range(0, 10):
    print(f'[{i + 1}]', end='')
    sleep(0.25)
lin()

print('Contagem de 10 até 0 de 2 em 2')
for i in range(10, -1, -2):
    print(f'[{i}]', end='')
    sleep(0.25)
lin()

print('Agora é sua vez:')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
