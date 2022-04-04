cond, cont, soma = 0, 0, 0;

while cond != 999:
    num = int(input(f'Digite um numero entre 0 e 999: '))
    cont +=1
    soma += num

    if num == 999:
        cond = 999
        soma = soma - 999

print(f'Foram digitados {cont-1} numeros')
print(f'A soma dos numeros digitadoes é: {soma}')