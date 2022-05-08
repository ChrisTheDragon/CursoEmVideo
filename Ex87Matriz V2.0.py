matriz = []
linha = []
coluna = []
pares = 0
maior2c = 0
maior2l = 0
soma3 = 0

for i in range(0, 3):
  for j in range(0, 3):
    linha.append(int(input(f'Digite o numero da posição [{i}][{j}]: ')))
  matriz.append(linha[:])
  linha.clear()

print('\nMatriz Gerada: ')
for i in range(0, 3):
  for j in range(0, 3):
    print(f'[{matriz[i][j]:^5}]', end='')
  print()

maior2c = matriz[0][1]
maior2l = matriz[1][0]
for i in range(0, 3):
  for j in range(0, 3):
    #Soma dos valores pares
    if matriz[i][j] % 2 == 0:
      pares += matriz[i][j]
    #Maior valor da segunda coluna
    if j == 1:
      if maior2c < matriz[i][1]:
        maior2c = matriz[i][1]
    #Soma dos valores da terceira coluna
    soma3 += matriz[i][2]
    #Maior valor da segunda linha
    if i == 1:
      if maior2l < matriz[1][j]:
        maior2l = matriz[1][j]

print(f'\nA noma de todos os valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior numero da segunda linha é {maior2l}')
print(f'O maior numero da segunda coluna é {maior2c}')
