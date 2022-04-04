prim = int(input(f'Digite o primeiro termo: '))
razao = int(input(f'Digite a Razão: '))
deci = prim + (10-1) * razao
max = 10
cont=0
cont1 = 0
total = 0

while cont1 < max:
    total += max
    while cont < max:
        prim += razao
        print(f'{prim}', end=' ')
        cont = cont + 1

    max = int(input(f'\nDeseja ver mais termos? Digite o numero: '))
    if max == 0:
        break

    cont1 = cont1 +1
    cont = 0
print(f'PA finalizada com {total} termos')