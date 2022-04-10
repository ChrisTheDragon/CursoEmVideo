lista = pares = impares = []
opcao = 'S'

#Sistema de continuação
while opcao == 'S':
    lista.append(int(input("Digite um número: ")))

    opcao = str(input(f'Deseja inserir mais um numero?'
          f'[S/N] -> ')).upper().strip()[0]

    while opcao not in 'sSnN':
        print('Opção Inválida! Tente novamente:')
        opcao = str(input(f'Deseja inserir mais um numero?'
                          f'[S/N] -> ')).upper().strip()[0]

for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'Lista Original = {lista}')
print(f'Pares = {pares}')
print(f'Impares = {impares}')