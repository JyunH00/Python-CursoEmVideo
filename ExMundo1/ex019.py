'''
Exercício 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''

##### Resolução #####

import random

### Criação das variáveis ###

pAluno = str(input('Primeiro aluno: '))

sAluno = str(input('Segundo aluno: '))

tAluno = str(input('Terceiro aluno: '))

qAluno = str(input('Quarto aluno: '))

lista = [pAluno, sAluno, tAluno, qAluno]

escolihdo = random.choice(lista)

### Print do resultado ###

print('O aluno(a) escolhido(a) foi: {} '. format(escolihdo))