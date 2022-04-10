lista = []

for i in range(0, 5):
    num = int(input('Digite um valor: '))

    for c, j in enumerate(lista):
        if num < j:
            lista.insert(c, num)
            break
    else: lista.append(num)


print(f'Voce digitou: {lista}')
