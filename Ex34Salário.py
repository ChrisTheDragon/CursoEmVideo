s = float(input('Digite o salário: R$'))

if s > 1250.00:
    print(f'Novo salário: R${s + (s * 10/100):.2f}')
    print(f'Aumento de: R${s * 10/100:.2f}')
else:
    print(f'Novo salário: R${s + (s * 15/100):.2f}')
    print(f'Aumento de: R${s * 15/100:.2f}')
