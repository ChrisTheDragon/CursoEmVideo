maiornome = ''
maioridade = 0
somaidade = 0
contIdade = 0

for c in range(1, 5):
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M] ou [F]: ').strip().upper())

    somaidade += idade

    if sexo == 'M':
        if idade > maioridade:
            maiornome = nome
            maioridade = idade

    if sexo == 'F' and idade < 20:
        contIdade += 1

    print(f'-'*25)

print(f'A média da idade do grupo é: {somaidade/4}')
print(f'O homem mais velho se chama {maiornome.upper()}')
print(f'O numero de mulheres com menos de 20 anos é {contIdade}')
