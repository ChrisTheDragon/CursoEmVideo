d = float(input('Digite a distancia: '))

if d <= 200 :
    p = d * 0.50
    print(f'O preço será R${p:.2f}')
else:
    p = d*0.45
    print(f'O preço será R${p:.2f}')
