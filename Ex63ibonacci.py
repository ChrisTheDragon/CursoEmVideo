max = int(input(f'Digite o numero máximo: '))
c = 0
ant = 0
prox = 1
soma = 0

while c <=max:
    print(f'{ant}', end=' ')
    soma = prox + ant
    ant = prox
    prox = soma
    c += 1