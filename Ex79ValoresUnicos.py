lista= []
opcao = ''
while True:
    lista.append(int(input('Digite um valor: ')))
    for i in range (len(lista)):
        if lista[len(lista)-1] in lista[:len(lista)-1]:
            lista.remove(lista[len(lista)-1])
            print(f'Valor duplicado!..')



    opcao = str(input(f'Deseja continuar?'
                      f'[S/N] -> ')).upper().split()[0]
    while opcao not in 'SsNn':
        print('Opção Invalida, Tente novamente')
        opcao = str(input(f'Deseja continuar?'
                          f'[S/N] -> ')).upper().split()[0]
    if opcao == 'N':
        print('='*25)
        print(f'Voce digitou: {sorted(lista)}')
        break