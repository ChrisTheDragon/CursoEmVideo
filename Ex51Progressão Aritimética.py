prim = int(input(f'Digite o primeiro termo: '))
razao = int(input(f'Digite a Razão: '))
deci = prim + (10-1) * razao

for c in range (prim, deci + razao, razao):
    print(f'{c}', end=' -> ')
print(f'FIM')