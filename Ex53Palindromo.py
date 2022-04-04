frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
frase = ''.join(palavras)
tamanho = len(frase)-1
inverso = ''

for c in range(tamanho, -1, -1):
    inverso += frase[c]

print(f'A frase {frase} invertida é: {inverso}')

if frase == inverso:
    print(f'\nÉ um palindromo')
else:
    print(f'\nNão é um palindromo')