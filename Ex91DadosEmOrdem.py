from random import randint
from time import sleep
j = 1
jogadas = {'Jogador 1': randint(1, 6),
           'Jogador 2': randint(1, 6),
           'Jogador 3': randint(1, 6),
           'Jogador 4': randint(1, 6)}
for i, v in jogadas.items():
    print(f'{i} jogou {v}')
    sleep(1)
print()
for i in sorted(jogadas, key=jogadas.get, reverse=True):
    print(f'{j}º Lugar: {i} com {jogadas[i]}')
    j += 1

