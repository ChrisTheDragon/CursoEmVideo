km = float(input('Digite a kilometragem: '))

if km > 80:
    print('seu carro foi multado')
    print(f'A multa é de R${(km - 80) * 7:.2f}')
else:
    print('OK')
