'''
Exercício 13b: Crie um programa que mostre o preço de um produto, e dê desconto de 15% se for pago à vista e 8% de aumento se pago parcelado
'''

##### Resolução #####

### Criação das variáveis ###

preco = float(input('Qual é o preco do produto? R$'))

aVista = preco * 0.85
parcelado = preco * 1.08 

### Print do resultado ###

print('-'*8)
print('Preço do produto: R${:.2f}.'.format(preco))
print('Preço à vista: R${:.2f}.'.format(aVista))
print('Preço se parcelado: R${:.2f}.'.format(parcelado))
print('-'*8)