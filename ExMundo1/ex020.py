'''
Exercício 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

##### Resolução #####

import random

### Criação das variáveis ###

pAluno = str(input('Primeiro aluno: '))

sAluno = str(input('Segundo aluno: '))

tAluno = str(input('Terceiro aluno: '))

qAluno = str(input('Quarto aluno: '))

lista = [pAluno, sAluno, tAluno, qAluno]
random.shuffle(lista)

### Print do resultado ###

print('A ordem de apresentação será: {} '.format(lista))