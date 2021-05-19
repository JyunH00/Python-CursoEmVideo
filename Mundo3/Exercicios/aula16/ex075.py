'''
Exercício 75: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

#### Resolução ####

#### Laço ####
c = 0
while c < 4:
    if c == 0:
        num1 = int(input('Digite um número: '))
    if c == 1:
        num2 = int(input('Digite outro número: '))
    if c == 2:
        num3 = int(input('Digite mais um número: '))
    if c == 3:
        num4 = int(input('Digite o último número: '))
    c += 1

#### Variáveis ####

numTupla = (num1, num2, num3, num4)

#### Prints ####
print(f'Você digitou os valores {numTupla}')
print(f'O valor 9 apareceu {numTupla.count(9)} vezes')

if 3 in numTupla:
    print(f'O valor 3 apareceu na {numTupla.index(3) + 1}º posição')
else:
    print('O valor 3 não foi digiado em nenhuma posição')

print(f'Os valores pares digitados foram:', end = ' ')
for i in numTupla:
    if i % 2 == 0:
        print(i, end = ' ')


'''
* Podemos pedir para o usuário escrever valores dentro da própria tupla!

numTupla = (int(input('Digite um número'), 
            int(input('Digite um número'),
            int(input('Digite um número'),
            int(input('Digite um número'))
'''