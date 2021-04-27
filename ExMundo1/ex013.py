'''
Exercício 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

##### Resolução #####

### Criação das variáveis ###

salario = float(input('Qual é o salário do funcionário? R$'))

aumento = salario * 1.15 # salario + (salario * 15/100)

### Print do resultado ###

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, aumento))