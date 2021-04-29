'''
Exercício 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela
cada um dos dígitos separados

Ex:
Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
'''

##### Resolução #####

### Criação das variáveis ###

num = int(input('Digite um número de 0 a 9999: '))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

### Print do resultado ###

print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))


'''
### Criação das variáveis ###

num = int(input('Digite um número de 0 a 9999: '))
num2 = str(num)

### Print do resultado ###

#** Dessa forma, se o número não tiver 4 digitos ele dará erro.
print('Unidade: {}'.format(num2[3]))
print('Dezena: {}'.format(num2[2]))
print('Centena: {}'.format(num2[1]))
print('Milhar: {}'.format(num2[0]))

'''
