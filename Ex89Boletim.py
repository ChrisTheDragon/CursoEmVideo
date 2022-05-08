nome = []
notas = []
alunos = []
op = 'S'

while op == 'S':
    nome.append(input('Nome: '))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    nome.append(notas[:])
    notas.clear()
    alunos.append(nome[:])
    nome.clear()
    op = str(input('Deseja Continuar?[S/N]: ')).upper()[0]
print('=-' * 35)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print(f'-' * 35)
for i in range(0, len(alunos)):
    print(f'{i:<4}{alunos[i][0]:<10}{(alunos[i][1][0] + alunos[i][1][1]) / 2:>8.2f}')
print(f'-' * 35)
while True:
    n = int(input(f'Pesquisa por Nº: (999 para interromper): '))
    for i in range(0, len(alunos)):
        if i == n:
            print(f'Notas de {alunos[i][0]}: {alunos[i][1]}')
            print(f'-' * 35)
    if n == 999:
        print(f'PROGRAMA FINALIZADO')
        break
