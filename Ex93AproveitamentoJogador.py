aproveitamento = {}
gols = []
total = 0
aproveitamento['nome'] = input('Nome do Jogador: ')
qpart = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou? '))

for i in range(qpart):
    gols.append(int(input(f'Quantos gols na partida {i+1}? ')))

aproveitamento['gols'] = gols[:]
aproveitamento['total'] = sum(gols)

print('=-'*20)
print(aproveitamento)
print('-='*20)

for i, k in aproveitamento.items():
    print(f'O campo {i} tem o valor {k}')
print('=-'*20)

print(f'O jogaodor {aproveitamento["nome"]} jogou {len(aproveitamento["gols"])} partidas!')
for i, v in enumerate(aproveitamento['gols']):
    print(f' => Na paritda {i+1}, fez {v} gols.')
print(f'Foi um total de {aproveitamento["total"]} gols.')