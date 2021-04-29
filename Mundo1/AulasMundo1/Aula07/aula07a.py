'''
Operadores aritméticos

Ordem de precedência:

1º ()
2° **
3º *, /, //, % (Resolver quem aparecer primeiro caso haja mais de 1)
4º +, -

'''

'''
Abrindo o console podemos fazer alguns testes com operações aritméticas

>>> 5+3*2
11

>>> 5**2
25

>>> 5**3
125

>>> 19//2
9

>>> 19/2
9.5

>>> 18%2
0

>>> 122%3
2

>>> 4**3
64

>>> pow(4, 3)
64

>>> 81**(1/2)
9.0
'''

'''
Podemos fazer algumas operações com Strings

>>> 'Oi' + 'Olá'
'OiOlá'

>>> 'Oi'*5
'OiOiOiOiOi

>>> '='*20
'===================='

>>> print('='*20)
===================
'''

#######################################################################
'''
{:número} > aparece a string no número colocado

{:>número} > alinha a direita

{:^número} > alinha centralmente

{:<número} > alinha a esquerda

{:=^número} > alinha centralmente com símbolo de '=' em volta

'''

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))

#######################################################################
#Especificando o tipo da variável com int()#
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

#######################################################
'''
>>> Podemos colocar o resultado dentro de .format()

>>> Podemos limitar o número de casa decimais com '{:.3f}'

>>> Para não pularmos uma linha entre 2 ou mais prints, basta colocar ('end = ' ' ') 
   
>>> "\n" no meio do print, quebra a linha  
'''

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end = ' ' )
print('Divisão inteira é {} e potência é {}'.format(di, e))
