numero = int(input(f'Digite um número: '))
cont = 0
for c in range(1, numero+1):
    if numero % c == 0:
        print(f'\033[1;31m', end=' ')
        cont += 1
    else:
        print(f'\033[36m', end=' ')

    print(f'{c}', end='')

if cont == 2:
    print(f'\n\033[0m{numero} é primo')
else:
    print(f'\n\033[0m{numero} não é primo')