'''
Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código. É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um laço no meio do caminho.

Além disso, vamos aprender como trabalhar com as novas fstrings do Python.
'''

'''
>>> Laços infinitos
        >>> while True
        >>> break ( Iterrompemos o laço)

>>> enquanto verdadeiro
        se ??
            passo
        se ??
            passo
        se ??
            passo
            interrompa
    pega

>>> while True:
        if ??
            passo
        if ??
            passo
        if ??  
            passo
            break
    pega
'''


#### Prática ####

cont = 1

while cont <= 10:
    print(cont, '->', end ='')
    cont += 1
print('Acabou')


while True:
    print(cont, '->', end ='')
    cont += 1
print('Acabou')

# Soma o 999
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
print('A soma vale {}'.format(s))


while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s +=n
print('A soma vale {}'.format(s))

#### UTILIZANDO fstring

#print('A soma vale {}'.format(s))

# Coloque o f antes das ''  e depois coloque as variáveis dentro das chaves.
print(f'A soma vale {s}')

nome = 'José'
idade = 33
salario = 987.3

# Podemos utilizar todas as ferramentos de modificação de print dentro das chaves também
print(f'O {nome:->20} tem {idade} anos e ganha R${salario:.2f}.')
print('O {} tem {} anos'.format(nome, idade))

