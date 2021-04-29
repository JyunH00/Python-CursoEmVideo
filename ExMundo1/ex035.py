'''
Exercício 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
formar um triângulo.
'''


##### Resolução #####

from math import fabs

print('-=-'*30)
print('Irei ler 3 comprimentos de reta e direi se elas podem ou não formar um triângulo.')
print('-=-'*30)

### Criação das variáveis ###

reta1 = float(input('Qual o comprimento da primeira reta? '))
reta2 = float(input('Qual o comprimento da segunda reta? '))
reta3 = float(input('Qual o comprimento da terceira reta? '))

if reta1 > fabs(reta2 - reta3)  and reta1 < (reta2 + reta3) and reta2 > fabs(reta1 - reta3)  and reta2 < (reta1 + reta3) and reta3 > fabs(reta1 - reta2)  and reta3 < (reta1 + reta2):
    print('Os comprimentos de reta {}, {}, {} podem formar um triângulo!'.format(reta1, reta2, reta3))
else:
    print('Os comprimentos de reta {}, {}, {} não podem formar um triângulo!'.format(reta1, reta2, reta3))