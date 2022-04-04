valor = int(input(f'Digite um numero: '))
fator = valor
valoro = valor

while valor != 1:
    fator = fator * (valor - 1)
    valor = valor - 1

print(f"{valoro}! = {fator}")