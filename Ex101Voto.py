from datetime import date


def voto(ano=0):
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos seu voto é NEGADO'
    elif 16 >= idade <= 17 or idade >= 65:
        return f'Com {idade} anos seu voto é OPCIONAL'
    elif idade >= 18:
        return f'Com {idade} anos seu voto é OBRIGATÓRIO'


id = int(input('Digite seu anos de nascimento: '))
print(voto(id))
