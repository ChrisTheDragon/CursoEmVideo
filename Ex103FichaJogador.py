def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) nesse campeonato')


print('='*10 + 'FICHA' + '='*10)
nom = str(input('Digite o nome do Jogador: '))
gol = str(input('Digite o numero de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nom.strip() == '':
    ficha(gols=gol)
else:
    ficha(nom, gol)
