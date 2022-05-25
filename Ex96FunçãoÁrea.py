def area(com, larg):
    a = com * larg
    print(f'A área de um terreno medindo {com}X{larg} é {a}m2')


print('Controle de Terrenos: ')
print('-'*20)
b = float(input('Comprimento:(m) '))
h = float(input('Altura:(m) '))
area(b, h)