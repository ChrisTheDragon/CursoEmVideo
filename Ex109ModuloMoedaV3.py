import moeda

n = float(input('Digite um valor: R$'))

print(f'O dobro de {n} é {moeda.dobro(n, True)}')
print(f'A metade de {n} é {moeda.metade(n, True)}')
print(f'Aumentando 10% fica {moeda.aumentar(n, 10)}')
print(f'Diminuindo 30% fica {moeda.diminuir(n, 30, True)}')