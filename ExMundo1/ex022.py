'''
Exercício 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

 nome com todas  letras maiúsculas
 nome com todas minúsuclas
 quantas letras no total (sem considerar espaços)
 quantas letras tem o primeiro nome
'''

##### Resolução #####

### Criação das variáveis ###

nomeC = str(input('Digite um nome completo: '))
nomeCJ = ''.join(nomeC.split())

### Print do resultado ###

print('-'*80)
print('O nome comepleto é: {}'.format(nomeC))
print('O nome com letras maiúsculas é: {}'.format(nomeC.upper()))
print('O nome com letras minúsuclas é: {}'.format(nomeC.lower()))
print('A quantidade letras do nome é: {}'.format(len(nomeCJ)))
print('Seu primeiro nome é {} e a quantidade de letras do primeiro nome é {}'.format(nomeC.split()[0], len(nomeC.split()[0])))
print('-'*80)

'''
Outras resoluções

print('A quantidade letras do nome é: {}'.format(len(nomeC) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nomeC.find(' ')))
'''