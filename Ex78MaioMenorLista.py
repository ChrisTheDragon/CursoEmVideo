lista = []

for i in range(0, 5):
    lista.append(int(input(f'Digite o {i+1}ª valor: ')))

print('=-'*25)
print(f'Você digitou: {lista}')
print(f'O maior valor foi {max(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'[{i}]', end='')
print(' ')
print(f'O menor valor foi {min(lista)} nas posções ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'[{i}]', end='')