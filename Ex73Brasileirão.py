times = ('América-MG','Athletico-PR','Atlético-GO',
         'Atlético-MG', 'Avaí', 'Botafogo', 'Ceará SC',
         'Corinthias', 'Coritiba', 'Cuiabá', 'Flamengo',
         'Fluminense', 'Fortaleza', 'Goiás', 'Internacional',
         'Juventude', 'Palmeiras', 'Bragantino','Santos','São Paulo')

print('==== BRASILEIRÂO SÈRIE A ====\n')
print(f'Os cinco primeiros colcoados são: {times[:5]}')
print(f'Os quatro ultimos colocados são: {times[16:]}')
print(f'Em ordem alfabética: {sorted(times)}')
print(f'O flamengo está na posição {times.index("Flamengo")+1}')
