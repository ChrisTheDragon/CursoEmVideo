soma = 0
for c in range(1,7):
    num = int(input(f'Digite um valor: '))
    if num % 2 == 0:
        soma += num
print(f'A soma somente dos numeros pares é: {soma}')