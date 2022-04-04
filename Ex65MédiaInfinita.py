cond = 'S'
cont, soma, maior, menor = 0, 0, 0, 100000000

while cond in 'Ss':
    num = int(input(f'Digite um numero: '))
    cont += 1
    soma += num

    if num > maior:
        maior = num

    if num < menor:
        menor = num

    cond = str(input(f'Quer Continuar [S/N] ').upper().strip()[0])

print(f'''foram digitados {cont} valores
A média dos valores digitados é: {soma/cont}
O maior valor foi: {maior}
O menor valor foi: {menor}''')