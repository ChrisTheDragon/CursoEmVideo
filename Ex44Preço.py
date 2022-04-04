p = float(input('Digite o preço do produto: R$'))
print('''Qual a forma de pagamento? 
1 - A vista em dinheiro
2 - A vista no cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão''')
i = int(input('Forma: '))

if i == 1:
    print(f'Proço final: R${p - (p*(10/100)):.2f}')
elif i == 2:
    print(f'Preço final: R${p - (p * (5/100)):.2f}')
elif i == 3:
    print(f'2 Parcelas de R${p/2}')
    print(f'Preço final: R${p}')
elif i == 4:
    pf = p + (p * 20/100)
    pa = int(input('Qual o numero de parcelas? '))
    print(f'{pa} Parcelas de R${pf/pa:.2f}')
    print(f'Preço final: {pf:.2f}')