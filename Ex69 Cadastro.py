M18 = Hom = Mul = 0

print('-=' * 10)
print('CADASTRO DE PESSOAS')
print('-=' * 10)

while True:
    idade = int(input(f'Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(f'Sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        M18 += 1
    if sexo in 'Mm':
        Hom += 1
    if sexo in 'Ff' and idade <= 20:
        Mul += 1

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input(f'Cadastrar mais uma pessoa? [S/N]: ')).upper().strip()[0]
    print('-' * 10)
    if opcao == 'N':
        break

print(f'{M18} pessoas com mais de 18 anos foram cadastradas')
print(f'{Hom} Homens foram cadastrados')
print(f'{Mul} Mulheres com menos de 20 anos foram cadastradas')
