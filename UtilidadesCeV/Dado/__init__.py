def leiaDinheiro(txt):
    valido = False
    while not valido:
        entrada = str(input(txt)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERROR: \"{entrada}\" não é uma entrada válida!\033[m')
        else:
            valido = True
            return float(entrada)
