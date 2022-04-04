total = maior = menor = 0
cont = 1
barato = ' '
while True:
    nome = str(input('Produto: '))
    preco = float(input('Preço: R$'))

    total += preco

    if preco >= 1000.00:
        maior += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = nome

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input(f'Inserir +1 produto? [S/N]: ')).upper().strip()[0]
    print('-' * 40)
    if opcao == 'N':
        break

print(f'O total gasto na compra foi R${total:.2f}')
print(f'O total de produtos custam mais de R$ 1000,00 é {maior}')
print(f'O produto mais barato é {barato}')