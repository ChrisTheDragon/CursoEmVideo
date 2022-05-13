from datetime import date
trabalhador = {}

trabalhador['Nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
trabalhador['Idade'] = date.today().year - ano
trabalhador['CTPS'] = int(input('CTPS: (0 para não tem): '))
if trabalhador['CTPS'] > 0:
    trabalhador['Contratacao'] = int(input('Ano de Contratação: '))
    trabalhador['Salario'] = float(input('Salário: R$'))
    Ap = date.today().year - trabalhador['Contratacao']
    if Ap >= 35:
        trabalhador['Aposentadoria'] = Ap
print('=-'*25)
for i, v in trabalhador.items():
    print(f'{i} tem valor {v}')