'''
Exercício 29: Escreva um programa que leia uma velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$7.00 por cada km acima do limite.
'''

##### Resolução #####

### Criação das variáveis ###

velocidadeC = float(input('Qual a velocidade do carro? '))

### Condições ###

if velocidadeC > 80:
    print('Você foi multado pois estava com uma velocidade de {}km/h'.format(velocidadeC))

    multa = (velocidadeC - 80) * 7

    print('Você foi multado em R${}'.format(multa))
else:
    print(('Você estava com uma velocidade de {}km/h e não foi multado'.format(velocidadeC)))