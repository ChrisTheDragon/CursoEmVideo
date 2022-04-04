prim = int(input(f'Digite o primeiro termo: '))
razao = int(input(f'Digite a Razão: '))
deci = prim + (10-1) * razao
cont=0

while cont < 10:
    prim += razao
    print(f'{prim}', end=' ')
    cont += 1

