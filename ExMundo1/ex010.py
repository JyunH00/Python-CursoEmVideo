'''
Exercício 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
Considere US$ 1.00 = R$ 3.27.
'''

##### Resolução #####

### Criação das variáveis ###

real = float(input('Quanto dinheiro você tem na carteira? R$'))

realDolar = dinheiro/3.27

### Print do resultado ###

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, realDolar))