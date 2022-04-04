import random

n = [1, 2, 3, 4, 5]

ne = random.choice(n)

na = int(input('Digite um numero entre 0 e 5: '))

if na == ne :
    print('Acertou Mizeravi')
else:
    print('ERRROOOUU')

print(f'O numero era {ne}')
