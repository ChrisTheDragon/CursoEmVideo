num = soma = cont = 0

while True:
    num = int(input(f'Digite um número [Digite 999 para parar]: '))
    if num == 999:
        break
    soma += num
    cont += 1

print(f'Foram digitados {cont} numeros e a sua soma é {soma}')