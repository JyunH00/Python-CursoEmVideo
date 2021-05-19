'''
Exercício 111: Crie um pacote chamado utilidadesCeV que tenhas dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
'''

from utilidadesCeV import moeda, dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 20, 12)

