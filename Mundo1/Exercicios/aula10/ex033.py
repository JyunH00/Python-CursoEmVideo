'''
Exercício 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

##### Resolução #####

print('-=-'*30)
print('Irei comparar 3 números e dizer qual o menor e qual é o maior!.')
print('-=-'*30)

### Criação das variáveis ###

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

### Condições ###

#Verificando menor número
if num1 <= num2 and num1 <= num3:
    menor = num1
if num2 <= num1 and num2 <= num3:
    menor = num2
if num3 <= num1 and num3 <= num2:
    menor = num3

#Verificando maior número
if num1 >= num2 and num1 >= num3:
    maior = num1
if num2 >= num1 and num2 >= num3:
    maior = num2
if num3 >= num1 and num3 >= num2:
    maior = num3

### Print do resultado ###

print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))

'''
Podemos eliminar o primeiro if se colocarmos menor = num1 e maior = num1 - Solução mais simples
'''