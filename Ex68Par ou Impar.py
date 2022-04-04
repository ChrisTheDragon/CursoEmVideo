import random

numJog = 0

while True:
    jogE = ' '
    jogC = ' '
    com = random.randint(1, 100)

    jogN = int(input(f'Digite um numero: '))
    while jogE not in 'PpIi':
        jogE = str(input(f'PAR ou IMPAR [P/I]: ')).strip().upper()[0]

    if jogE == 'P':
        jogC = 'I'
    elif jogE == 'I':
        jogC = 'P'

    result = com+jogN

    if result % 2 == 0:
        resultE = 'P'
    else:
        resultE = 'I'

    print(f'-='*20)
    print(f'''Voce jogou {jogN} e escolheu {jogE}. 
O computador jogou {com} e escolheu {jogC}.
SOMA: {result} / {resultE}''')
    print(f'=-'*20)

    if jogE[0] == resultE:
        print(f'Voce Ganhou! ')
        print(f'Joge novamente: \n')
    else:
        break

    numJog += 1

print(f'GAME OVER! Voce ganhou {numJog} vezes')
print(f'Fim do Programa')