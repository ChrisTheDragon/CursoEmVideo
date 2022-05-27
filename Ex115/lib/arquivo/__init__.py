from Ex115.lib.interface import *

def arquvioExiste(txt):
    try:
        a = open(txt, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(txt):
    try:
        a = open(txt, 'wt+')
        a.close()
    except:
        print('Arquivo não criado')
    else:
        print(f'Arquivo {txt} criado com sucesso!')


def lerArquivo(txt):
    try:
        a = open(txt, 'rt')
    except:
        print('ERRO ao abrir o arquivo')
    else:
        cabeçalho('LISTA DE PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()


def cadastrar(txt, nome='<desconhecido>', idade=0):
    try:
        a = open(txt, 'at')
    except:
        print('ERRO ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO ao escrever dados')
        else:
            print(f'{nome} adicionado com sucesso!')
            a.close()