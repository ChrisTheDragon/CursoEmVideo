import moeda

n = float(input('Digite um valor: R$'))

print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'Aumentando 10% fica {moeda.moeda(moeda.aumentar(n, 10))}')
print(f'Diminuindo 30% fica {moeda.moeda(moeda.diminuir(n, 30))}')
