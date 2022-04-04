
valores = (int(input('Escreva o 1º número: ')),
           int(input('Escreva o 2º número: ')),
           int(input('Escreva o 3º número: ')),
           int(input('Escreva o 4º número: ')))

print(f'O valor 9 apareceu {valores.count(9)} vezes')

if 3 in valores:
    print(f'O valor 3 apareceu na posição {valores.index(3) + 1}')
else: print('O valor 3 não aparece')

print(f'O números pares são: ', end='')
for i in valores:
    if i % 2 == 0:
        print(i, end=' ')
