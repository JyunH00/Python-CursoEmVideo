'''
Exercício 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e o último nome separadamente

Ex: Ana Maria de Souza
primeiro: Ana
último: Souza
'''

##### Resolução #####

### Criação das variáveis ###

nome = str(input('Digite seu nome: '))
nome = nome.split()

primeiroNome = nome[0]
ultimoNome = nome[len(nome) - 1]

### Print do resultado ###

print('Seu primeiro nome é: {}'.format(primeiroNome))
print('Seu ultimo nome é: {}'.format(ultimoNome))