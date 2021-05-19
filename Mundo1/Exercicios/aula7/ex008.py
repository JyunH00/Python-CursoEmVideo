'''
Exercício 8: Escreva um programa que leia um valor em metros e o exiba convertido em outras medidas como: centímetros e milímetros.
'''

##### Resolução #####

### Criação das variáveis ###

vMetros = float(input('Uma distância em metros:'))

vKm = vMetros / 1000
vHm = vMetros / 100
vDam = vMetros / 10
vDm = vMetros * 10
vCm = vMetros * 100
vMm = vMetros * 1000

### Print do resultado ###

print('A medida de {:.1f}m corresponde a '.format(vMetros))

print('{}km'.format(vKm))
print('{}hm'.format(vHm))
print('{}dam'.format(vDam))
print('{:.0f}dm'.format(vDm))
print('{:.0f}cm'.format(vCm))
print('{:.0f}mm'.format(vMm))