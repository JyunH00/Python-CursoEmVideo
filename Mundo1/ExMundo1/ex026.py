'''
Exercício 26: Faça um programa que leia uma frase pelo teclado e mostre:

> Quantas vezes aparece a letra "a";
> Em que posição ela aparece a primeira vez;
> Em que posição aparece a última vez.
'''

##### Resolução #####

### Criação das variáveis ###

frase = str(input('Digite sua frase: ')).lower()

apareceA = frase.count('a')

primeiroA = frase.find('a')

ultimoA = frase.rfind('a')

### Print do resultado ###

print(frase)
print('Número de vezes que aparece a letra a: {}'.format(apareceA))
print('Em que posição está a primeira letra a: {}'.format(primeiroA + 1))
print('Em que posição está a última letra a: {}'.format(ultimoA + 1))