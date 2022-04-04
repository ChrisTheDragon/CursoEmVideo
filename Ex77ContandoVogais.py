lista = ('Mundo', 'Samba', 'Sorteio',
         'Granada', 'Rato', 'Soma', 'Dado')
palavra =' '
for i in lista:
    print(f'\nNa palavra {i.upper()} tem ', end='')
    for j in i:
        if j in 'aeiou': print(j, end=' ')