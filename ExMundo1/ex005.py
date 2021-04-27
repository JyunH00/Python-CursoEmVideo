'''
Exercício 5: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor
e seu antecessor
'''

##### Resolução #####

### Criação das variáveis ###
numero = int(input('Digite um número: '))

sucessor = numero + 1
antecessor = numero - 1

### Print do resultado ###

print('Analisando o valor {}, seu antecessor é {} e seu sucessor é {}'.format(numero, antecessor, sucessor))

'''
Pode-se usar (numero, n+1, n-1), caso não se crie as variáveis 'antecessor' e 'sucessor'  
'''