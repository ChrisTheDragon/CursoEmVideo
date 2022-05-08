lista = [[],[]]

for i in range(0, 7):
  num = int(input(f'Digite um numero: '))
  if num % 2 == 0:
    lista[0].append(num)
  else:
    lista[1].append(num)

print(f'Numeros Pares: {sorted(lista[0])}')
print(f'Numeros Impares: {sorted(lista[1])}')