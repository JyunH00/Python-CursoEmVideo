# Importações

import menu
import validacao
from time import sleep
cores = {'finaliza':'\033[m',
         'azul':'\033[1;34m',
         'amarelo':'\033[1;33m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'magenta':'\033[1;35m'
         }

#Programa Principal

arq = 'clientes.txt'

if not validacao.arqExiste(arq):
    validacao.criarArq(arq)

while True:
    resposta = menu.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        menu.cabeçalho('Opção 1')
        validacao.lerArq()
    elif resposta == 2:
        menu.cabeçalho('Opção 2')
    elif resposta == 3:
        menu.cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print(f'{cores["vermelho"]}ERRO! Digite uma opção válida!{cores["finaliza"]}')
    sleep(2)

