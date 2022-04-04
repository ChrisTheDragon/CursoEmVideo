from random import choice
'''1 - Pedra / 2 - Papel / 3 - Tesoura'''
mao = [1, 2, 3]

maoa = choice(mao)

print('Escolha sua jogada: ')
print('1 - Pedra / 2 - Papel / 3 - Tesoura')
maoe = int(input('Digite o numero correspondente a sua jogada: '))

if maoe == 1 and maoa == 2:
    print('Pedra x Papel')
    print('Você Perdeu')
elif maoe == 1 and maoa == 3:
    print('Pedra x Tesoura')
    print('Você Ganhou')
elif maoe == 2 and maoa == 1:
    print('Papel x Pedra')
    print('Você Ganhou')
elif maoe == 2 and maoa == 3:
    print('Papel x Tesoura')
    print('Você Perdeu')
elif maoe == 3 and maoa == 1:
    print('Tesoura x Pedra')
    print('Você Perdeu')
elif maoe == 3 and maoa == 2:
    print('Tesoura x Papel')
    print('Você Ganhou')
elif maoe == maoa:
    print('Empate')