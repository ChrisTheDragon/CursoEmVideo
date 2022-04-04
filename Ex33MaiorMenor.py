n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um Numero: '))

if n1 > n2 and n1 > n3:
    print(f'O numero maior é : {n1}')
else:
    if n2 > n1 and n2 > n3:
        print(f'O numero maior é {n2}')
    else:
        if n3 > n1 and n3 > n2:
            print(f'O numero maior é: {n3}')

if n1 < n2 and n1 < n3:
    print(f'O numero menor é : {n1}')
else:
    if n2 < n1 and n2 < n3:
        print(f'O numero menor é {n2}')
    else:
        if n3 < n1 and n3 < n2:
            print(f'O numero menor é: {n3}')