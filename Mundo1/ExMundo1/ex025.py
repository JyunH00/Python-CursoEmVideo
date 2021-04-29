'''
Exercício 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
'''

##### Resolução #####

### Criação das variáveis ###

nome = str(input('Digite seu nome completo: '))
nome = nome.lower()


### Print do resultado ###

print('Seu nome tem Silva? {}'.format('silva' in nome) )
