pessoas = []
indv = {}
op = 'S'
somId = 0

while op != 'N':
    indv['nome'] = str(input('Nome: '))

    indv['sexo'] = str(input('Sexo:[M/F]: ')).upper()[0]
    while indv['sexo'] not in 'MF':
        print(f'ERRO! Por favor entre com M ou F')
        indv['sexo'] = str(input('Sexo:[M/F]: ')).upper()[0]

    indv['idade'] = int(input('Idade: '))

    pessoas.append(indv.copy())

    op = str(input(f'Deseja continuar?[S/N]-> ')).upper()[0]
    while op not in 'SN':
        print(f'ERRO! Por favor entre com S ou N')
        op = str(input(f'Deseja continuar?[S/N]-> ')).upper()[0]

qpes = len(pessoas)

for i in range(0, len(pessoas)):
    somId += pessoas[i]['idade']
medId = somId/qpes

print('-='*25)
print(f'A) Foram cadastradas {qpes} pessoas')
print(f'B) A média de idade é: {medId:.2f}')
print('C) As mulheres cadastradas foram: ', end='')
for i in range(0, len(pessoas)):
    if pessoas[i]['sexo'] == 'F':
        print(f'|{pessoas[i]["nome"]}| ', end='')
print('')
print('D) Lista de Pessoas que estão acima da média de idade: ')
for i in range(0, len(pessoas)):
    if pessoas[i]['idade'] > medId:
        print(f'Nome:{pessoas[i]["nome"]} | Sexo:{pessoas[i]["sexo"]} | Idade:{pessoas[i]["idade"]}')
