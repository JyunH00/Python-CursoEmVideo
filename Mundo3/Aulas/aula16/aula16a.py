'''
Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. As tuplas são variáveis compostas e
imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
'''

'''
** Variáveis compostas
    >>> TUPLAS, listas, dicionários
    >>> Não podemos atribuir múltiplos valores em variáveis simples
        >>> lanche = 'hamburguer'
        >>> lanche = 'suco' -> lanche vira 'suco'
   
** Tuplas
    >>> Utlizamos ()
    >>> Variável que guarda vários valores
    >>> Itens identificados por índices (0 -> ?)
    
    >>> print(lanche)
    >>> print(lance[2])
    >>> print(lanche[0:2]
    >>> print(lanche[1:]
    >>> print(lanche[-1] -> último elemento (-1 (ultimo), -2 (penultimo)...)
    
    >>> for c in lanche:
            print(c)    
    >>> Podemos usar o for não apenas com range.
    >>> Irá imprimir todo os valores da variável lanche
    
*** TUPLAS SÃO IMUTÁVEIS (Não podemos mudar a tupla)
'''

#### Prática ####
'''
# O suco substitui hamburguer
lanche = 'Hambúrguer'
lanche = 'Suco'
'''

# Declaração da tupla

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') # lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'

# Testes de prints

print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[-2:])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])

# Tuplas são imutáveis
'''
lanche[1] = 'Refrigerante' # TypeError: 'tuple' object does not support item assignment
'''

#Uso do for

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]} na posição {contador }')
print('Comi pra caramba!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

print(sorted(lanche)) # Exibe em na forma ordenada (alfabética)

############################################################################################

a = (2, 5, 4)
b = (5, 8, 1, 2)

c = (a + b) # Cola as 2 tuplas (primeiro a depois b)
print(c)

c = (b + a) # COla as 2 tuplas (primeiro b depois a)
print(c)

print(c.count(5)) # Número de vezes em que aparece 5
print(c.index(4)) # Primeira ocorrência
print(c.index(5, 1)) # Primeira ocorrência a partir da posição 1

pessoa = ('Gustavo', 39, 'M', 99.88)

#del(pessoa) # Apaga a tupla
#del(pessoa[0]) # Erro # Não podemos apagar apenas um elemento da tupla
print(pessoa)
