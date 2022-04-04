lista = ('Pão', 0.50,
         'Arroz', 8.10,
         'Macarrão', 4.5,
         'Café', 3.4,
         'Charque', 120)

print(f'{"LISTA DE COMPRAS":^35}')
print('='*35)
for i in range(0, len(lista)):
    if (type(lista[i]) == str):
        print(f'{lista[i]:-<30}R${lista[i+1]:>7.2f}')
print('='*35)