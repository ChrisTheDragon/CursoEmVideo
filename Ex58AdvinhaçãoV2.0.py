from random import randint

ne = randint(0, 10)

certo = False
palpite = 0

while not certo:
    na = int(input(f'Digite um numero entre 0 e 10: '))
    palpite +=1
    if na == ne:
        certo = True
    else:
        if na < ne:
            print(f'Numero maior')
        elif na > ne:
            print(f'Numero menor')

print(f'Acertou!!')
print(f'Numero de palpites: {palpite}')
