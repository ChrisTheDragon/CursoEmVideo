vcasa = float(input('Digite o Valor da Casa: '))
sal = float(input('Digite o salário: '))
anos = int(input('Digite o o numero de anos para pagar: '))

pres = vcasa/(anos*12)

print(f'A prestação será de: {pres:.2f}')

if pres > (sal*30/100):
    print('Emprestimo NEGADO')
else:
    print('Emprestimo APROVADO')
