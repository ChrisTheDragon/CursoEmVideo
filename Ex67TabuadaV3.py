num = i = 0
while True:
    num = int(input(f'Digite um numero para ver sua tabuada: '))
    if num < 0:
        break
    for i in range(0, 11):
        print(f'{i} x {num} = {i*num}')
print(f'FIM')