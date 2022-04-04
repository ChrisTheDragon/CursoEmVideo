from datetime import date
cont = 0

for c in range(1,8):
    ano = int(input(f'digite o ano {c}º de nascimento: '))
    if date.today().year - ano >= 21:
        cont += 1

print(f'{cont} são maiores de idade')
print(f'{7-cont} ainda não são maiores de idade')