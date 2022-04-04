p = float(input('Digite o seu Peso: '))
a = float(input('Digite a sua Altura: '))

imc = p / (a*a)

print(f'Seu IMC é {imc:.1f}')
if imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Peso Ideal')
elif 25<= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Mórbida')