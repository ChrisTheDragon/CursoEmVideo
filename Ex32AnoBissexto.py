from datetime import date
n = int(input('Digite um ano (Digite 0 para o ano atual): '))
if n == 0:
    n = date.today().year
if (n % 4 == 0 and n % 100 != 0) or n % 400 ==0:
    print(f'{n} É bissexto')
else:
    print(f'{n} Não é bissexto')
