from Ex115.lib.interface import *
from Ex115.lib.arquivo import *

arq = 'bancodedados.txt'

if not arquvioExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])

    if resposta == 1:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 2:
        lerArquivo(arq)
    elif resposta == 3:
        print('\033[0;32mSAINDO...\nNunca é um Adeus\033[m')
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida!\033[m')