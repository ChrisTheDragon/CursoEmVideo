n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2)/2

if m < 5.0:
    print(f'Sua média foi de {m}, Aluno REPROVADO')
elif 5.0 <= m < 6.9:
    print(f'Sua média foi de {m}, Aluno em RECUPERAÇÃO')
else:
    print(f'Sua média foi de {m}, aluno APROVADO')
