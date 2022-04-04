from datetime import date

a = int(input('Digite o ano do seu nascimento: '))
t = date.today().year - a
f = 18 - t

if t < 18:
    print(f'Ainda falta {f} para se alistar')
elif t > 18:
    print(f'Já se passou {f*(-1)} anos do seu alistamento.')
else:
    print('Seu alistamento é esse ano.')

