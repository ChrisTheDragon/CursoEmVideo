lista = []
opcao = 'S'

while opcao == 'S':
    lista.append(input("Digite um número: "))

    opcao = str(input(f'Deseja inserir mais um numero?'
                      f'[S/N] -> ')).upper().strip()[0]

    while opcao not in 'sSnN':
        print('Opção Inválida! Tente novamente:')
        opcao = str(input(f'Deseja inserir mais um numero?'
                          f'[S/N] -> ')).upper().strip()[0]

print(f'Foram digitados {len(lista)} numeros')
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
