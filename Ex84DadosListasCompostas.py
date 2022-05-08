lista = []
dado = []
pesado = 0
leve = 9999
op = 'S'

while op == 'S':
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(dado) == 0:
        pesado = leve = dado[1]
    else:
        if dado[1] > pesado:
            pesado = dado[1]
        if dado[1] < leve:
            leve = dado[1]
    lista.append(dado[:])
    dado.clear()

    op = str(input('Deseja Continuar?[S/N]: ')).upper()[0]

print('=-' * 30)
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'O maior peso foi {pesado} de ', end='')
for i in lista:
    if i[1] == pesado:
        print(f'[{i[0]}]', end='')
print(f'\nO menor peso foi {leve} de ', end='')
for i in lista:
    if i[1] == leve:
        print(f'[{i[0]}]', end='')