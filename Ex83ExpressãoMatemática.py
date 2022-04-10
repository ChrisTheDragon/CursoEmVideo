expr = str(input('Digite a expressão: '))
lista = []
pa = pf = 0

for i in expr:
    if i == '(':
        lista.append('(')
    elif i == ')':
        lista.append(')')


for i in lista:
    if i == '(':
        pa +=1
    elif i == ')':
        pf +=1

if pa == pf:
    print('Sua Expressão está correta!')
else:
    print('Sua Expressão está incorreta!')