opcao = 0
valor1 = int(input(f'Digite o primeiro Valor: '))
valor2 = int(input(f'Digite o segundo valor: '))

while opcao != 5:
    print(f'-' * 10, 'MENU', '-' * 10)
    print(f'Digite uma das Opções abaixo:')
    print(f'    [1] - Somar     ')
    print(f'    [2] - Multiplicar     ')
    print(f'    [3] - Maior     ')
    print(f'    [4] - Novos Numeros     ')
    print(f'    [5] - Sair     ')
    opcao = int(input('-> '))
    if opcao == 1:
        print(f'A soma é: {valor1 + valor2}')

    elif opcao == 2:
        print(f'A multiplicação é: {valor1 * valor2}')

    elif opcao == 3:
        if valor1 > valor2:
            print(f'O maior valor é {valor1}')
        else:
            print(f'O maior valor é {valor2}')
    elif opcao == 4:
        print(f'Infrome os numeros novamente: ')
        valor1 = int(input(f'Digite o primeiro Valor: '))
        valor2 = int(input(f'Digite o segundo valor: '))
    elif opcao == 5:
        print(f'Finalizando')
    else:
        print(f'Opção Inválida!')

print(f'Programa Finalizado')
