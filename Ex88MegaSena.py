from random import randint
from time import sleep

lista = []
todos = []
j = 0

jogos = int(input('Qauntos Jogos Serão Gerados? '))

for i in range(0, jogos):
    while len(lista) < 6:
        n = randint(0, 60)
        if n not in lista:
            lista.append(n)
    lista.sort()
    todos.append(lista[:])
    lista.clear()
print('---------JOGOS GERADOS---------')
for i in range(0, len(todos)):
    print(f'Jogo Nª{i+1}: {todos[i]}')
    sleep(1)
print(f'-'*7, 'BOA SORTE', '-'*7)
