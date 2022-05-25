from time import sleep
n = []


def maior (num):
    for i in num:
        print(f'[{i}]', end='')
        print('')
        sleep(0.25)
    print(f'Foram informados {len(num)}')
    print(f'O maior é {max(num)}')


while True:
    n.append(int(input('Digite um número: ')))
    op = str(input('Deseja continuar?[S/N] ')).upper()[0]
    if op != 'S':
        break
maior(n)