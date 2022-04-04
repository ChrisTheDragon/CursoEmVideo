from random import randint
j = ('Pedra', 'Papel', 'Tesoura')
jc = randint(0, 2)

print('=-'*20)
print('             JO - KEN - PO')
print('=-'*20)
print('''Digite:
0 - PEFRA
1 - PAPEL
2 - TESOURA''')
j1 = int(input('Qual sua Jogada? '))
print('-='*20)
print(f'     VOCE : {j[j1]} x {j[jc]} : COM')
print('=-'*20)

if jc == 0:
    if j1 == 0:
        print('Empate')
    elif j1 == 1:
        print('Voce Ganhou')
    elif j1 == 2:
        print('Voce Perdeu')
    else:
        print('JOGADA INVÁLIDA')
elif jc == 1:
    if j1 == 0:
        print('Voce Perdeu')
    elif j1 == 1:
        print('Empate')
    elif j1 == 2:
        print('Voce Ganhou')
    else:
        print('JOGADA INVÁLIDA')
elif jc == 2:
    if j1 == 0:
        print('Voce Ganhou')
    elif j1 == 1:
        print("Voce Perdeu")
    elif j1 == 2:
        print('Empate')
    else:
        print('JOGADA INVÁLIDA')