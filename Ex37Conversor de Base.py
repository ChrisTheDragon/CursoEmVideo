n = int(input('Digite um numero: '))
print('Escolha uma das opções: ')
a = int(input('1 - binario / 2 - octal / 3 - hexadecimal: '))

if a == 1:
    print(f'Em binario: {bin(n)[2:]}')
if a == 2:
    print(f'Em Octal: {oct(n)[2:]}')
if a == 3:
    print(f'Em Hexadecimal: {hex(n)[2:]}')
if a != 1 and a != 2 and a != 3:
    print('Opção Inválida')