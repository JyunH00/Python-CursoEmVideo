'''
Exercício 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''

##### Resolução #####

### Criação das variáveis ###

pNota = float(input('Primeira nota do aluno:'))
sNota = float(input('Segunda nota do aluno:'))

mNotas = (pNota + sNota)/2

### Print do resultado ###

print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(pNota, sNota, mNotas))