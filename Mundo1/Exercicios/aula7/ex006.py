'''
Exercício 6: Crie um algoritmo que leia um número e mostre seu dobro, triplo e a raiz quadrada
'''

##### Resolução #####

### Criação das variáveis ###

numero = int(input('Digite um número: '))

dobro = numero*2
triplo = numero*3
raiz = numero**(1/2) # raiz = pow(numero, 1/2)


### Print do resultado ###

print('O dobro de {} vale {}.'.format(numero, dobro))
print('O triplo de {} vale {}.'.format(numero, triplo))
print('A raiz quadrada de {} vale {:.2f}.'.format(numero, raiz))

'''
Pode-se usar (numero, numero*2), (numero, numero*3) e (numero, numero**1/2) ou (numero, pow(numero, 1/2), caso não se crie as variáveis 
'''