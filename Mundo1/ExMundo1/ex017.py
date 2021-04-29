'''
Exercício 17:  Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
'''


##### Resolução #####

import math

### Criação das variáveis ###

catOposto = float(input('Comprimento do cateto oposto: '))

catAdj = float(input('Comprimento do cateto adjacente: '))

hipotenusa = math.hypot(catOposto, catAdj)

### Print do resultado ###

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

'''
Outra resolução

hipotenusa = (catOposto ** 2 + catAdj ** 2) ** (1/2) 
'''