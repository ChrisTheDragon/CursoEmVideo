from datetime import date
a = int(input('Digite o ano de nascimento: '))

i = date.today().year - a

print(f'Sua Idade é: {i}')
if i <= 9:
    print('Categoria MIRIM')
elif i <= 14:
    print('Categoria INFANTIL')
elif i <= 19:
    print('Categoria JUNIOR')
elif i == 20:
    print('Categoria SENIOR')
elif i > 20:
    print('Categoria MASTER')