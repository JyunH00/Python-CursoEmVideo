'''
Exercício 66: Crie um programa que leia vários números interios pelo teclado. O programa só vai parar quando digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o 999)
'''

#### Resolução ###

print('-=-'*20)
print('Utilização de While TRUE')
print('-=-'*20)

### Variáveis ###

numInt = soma = contador = 0

### Laço While ###

while True:
    numInt = int(input('Digite um número inteiro (999 para parar): '))
    if numInt == 999:
        break
    soma += numInt
    contador += 1
print(f'A soma dos {contador} valores foi {soma}!')