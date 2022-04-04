numEx = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um  numero entre 0 e 20: '))

while num < 0 or num > 20:
    print('Numero inválido!')
    num = int(input('Digite um  numero entre 0 e 20: '))

for i in range (0, len(numEx)):
    if (i == num):
        print(f'Você digitou o número {numEx[i]}')