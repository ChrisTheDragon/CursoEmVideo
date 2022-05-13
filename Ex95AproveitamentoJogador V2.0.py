aproveitamento = {}
todos = []
gols = []
total = 0
op = 'S'
cod = 0

while op != 'N':
    aproveitamento['nome'] = input('Nome do Jogador: ')
    qpart = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou? '))
    for i in range(qpart):
        gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))
        total += gols[i]
    aproveitamento['gols'] = gols[:]
    aproveitamento['total'] = total

    todos.append(aproveitamento.copy())
    gols.clear()
    total = 0

    op = str(input('Deseja Continuar?[S/N]: ')).upper()[0]
    while op not in 'SN':
        print(f'ERRO! Por favor entre com S ou N')
        op = str(input(f'Deseja continuar?[S/N]-> ')).upper()[0]

print('=-' * 20)
print(f'{"Cod.":<6}{"Nome":<13}{"Gols":<15}{"Total":<13}')
print('-' * 40)
for i in range(len(todos)):
    print(f'{i:<6}{todos[i]["nome"]:<13}{str(todos[i]["gols"]):<15}{todos[i]["total"]:<13}')
print('=-' * 20)

while cod != 999:
    cod = int(input('Mostrar levantamento de qual jogador? '))
    if cod == 999:
        break
    if cod >= len(todos):
        print(f'ERRO. Não existe jogador com código {cod}')
    else:
        print(f'--Levantamento do jogador {todos[cod]["nome"]}')
        for i, g in enumerate(todos[cod]['gols']):
            print(f'No jogo {i} ele fez {g} gols.')
        print('-' * 40)