from ex115 import menu

def arqExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArq(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {arq} criado com sucesso! ')

def lerArq(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('ERRO ao ler arquivo!')
    else:
        menu.cabeçalho('PESSOAS CADASTRADAS')
        print(a.readlines())