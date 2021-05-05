'''
Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python.
Por exemplo:

c=1 while c !=10:

print(c)

c+=1

print(‘Acabou’)

'''

'''
>>> Utilizamos o laço de repetição while quando não sabemos o limite do laço
    >>> Estrutura de repetição com teste lógico
    >>> Utilizamos uma condição até ela se satisfazê-la
    >>> A condição é verdadeira até que se torne falsa

>>> enquanto não ??
        passo
    pega
    
>>> while not ??
        passo
    pega
    
'''

#### Prática ####

# Quando sabemos o limite podemos usar for
for c in range(0, 5):
    print(c)
print('FIM')

#Quando sabemos o limite podemos usar while
c = 0
while c < 5:
    print(c)
    c += 1 # Incremetamos a condição, se não temos um loop infinito
print('FIM')

#Quando não sabemos o limite não podemos usar for, mas podemos usar while
'''
n = 1
while n != 0: # Flag / Ponto de parada / Condição de parada
    n = int(input('Digite um valor: ')) # While só irá terminar quando o usuário digitar 0
print('FIM')
'''
'''
n = 1
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')
'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par,impar))



