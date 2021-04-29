'''
Exercício 14: Crie um programa que converta uma temperatura em ºC para ºF
'''

##### Resolução #####

### Criação das variáveis ###

tCelcius = float(input('Informe a temperatura em ºC:'))

tFah = (tCelcius * 9 / 5) + 32

### Print do resultado ###

print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF!'.format(tCelcius, tFah))
