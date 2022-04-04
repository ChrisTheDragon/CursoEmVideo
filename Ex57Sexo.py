sexo = str(input(f'Digite se sexo [M/F] = ').upper())

print(sexo)

while sexo != 'M' and sexo != 'F':
    print(sexo)
    print(f'Resposta Inválida')
    sexo = input(f'Digite novamente:').upper()

print(f'O sexo digitado foi: {sexo}')