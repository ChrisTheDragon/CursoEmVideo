matriz = []
linha = []

#for i in range(0, 3):
#  for j in range(0, 3):
#    matriz[i][j] = int(input(f'Digite um valor: '))

for i in range(0, 3):
  for j in range(0, 3):
    linha.append(input(f'Digite o numero da posição [{i}][{j}]: '))
  matriz.append(linha[:])
  linha.clear()

print('\nMatriz Gerada: ')
for i in range(0, 3):
  for j in range(0, 3):
    print(f'[{matriz[i][j]:^5}]', end='')
  print()