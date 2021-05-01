'''
Exercício 42: Refaça o DESAFIO 035 dos triãngulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

> Equilátero: Todos os lados iguais
> Isósceles: Dois lados iguais
> Escalenos: Todos os lados diferentes

'''

##### Resolução #####

from math import fabs

cores = {'finaliza':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'magenta':'\033[35m'
         }

print('-=-'*30)
print('====CATEGORIA DE NATAÇÃO====')
print('Irei ler 3 comprimentos de reta e direi se elas podem ou não formar um triângulo, além disso direi se:')
print('''> {}Equilátero{}: Todos os lados iguais\n
> {}Isósceles{}: Dois lados iguais\n
> {}Escalenos{}: Todos os lados diferentes
'''.format(cores['vermelho'], cores['finaliza'], cores['amarelo'], cores['finaliza'], cores['azul'], cores['finaliza']))
print('-=-'*30)

### Criação das variáveis ###

reta1 = float(input('Qual o comprimento da primeira reta? '))
reta2 = float(input('Qual o comprimento da segunda reta? '))
reta3 = float(input('Qual o comprimento da terceira reta? '))

if reta1 > fabs(reta2 - reta3)  and reta1 < (reta2 + reta3) and reta2 > fabs(reta1 - reta3)  and reta2 < (reta1 + reta3) and reta3 > fabs(reta1 - reta2)  and reta3 < (reta1 + reta2):
    print('Os comprimentos de reta {}, {}, {} podem formar um triângulo!'.format(reta1, reta2, reta3))
    if reta1 == reta2 == reta3:
        print('Tais retas forma um triângulo {}EQUILÀTERO{}!'.format(cores['vermelho'], cores['finaliza']))
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Tais retas forma um triângulo {}ISÓSCELES{}!'.format(cores['amarelo'], cores['finaliza']))
    elif reta1 != reta2 != reta3:
        print('Tais retas forma um triângulo {}ESCALENO{}!'.format(cores['azul'], cores['finaliza']))
else:
    print('Os comprimentos de reta {}, {}, {} não podem formar um triângulo!'.format(reta1, reta2, reta3))




'''
Outra resolução

if reta1 > fabs(reta2 - reta3)  and reta1 < (reta2 + reta3) and reta2 > fabs(reta1 - reta3)  and reta2 < (reta1 + reta3) and reta3 > fabs(reta1 - reta2)  and reta3 < (reta1 + reta2):
    print('Os comprimentos de reta {}, {}, {} podem formar um triângulo!'.format(reta1, reta2, reta3))
    if reta1 == reta2 == reta3:
        print('Tais retas forma um triângulo {}EQUILÀTERO{}!'.format(cores['vermelho'], cores['finaliza']))
    elif reta1 != reta2 != reta3:
        print('Tais retas forma um triângulo {}ESCALENO{}!'.format(cores['azul'], cores['finaliza']))
    else: 
        print('Tais retas forma um triângulo {}ISÓSCELES{}!'.format(cores['amarelo'], cores['finaliza']))
else:
    print('Os comprimentos de reta {}, {}, {} não podem formar um triângulo!'.format(reta1, reta2, reta3))
'''