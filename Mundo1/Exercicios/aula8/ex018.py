'''
Exercício 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''


##### Resolução #####

import math

### Criação das variáveis ###

angulo = float(input('Digite o ângulo que você deseja: '))

anguloR = math.radians(angulo)

seno = math.sin(anguloR)
cosseno = math.cos(anguloR)
tangente = math.tan(anguloR)

### Print do resultado ###

print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))