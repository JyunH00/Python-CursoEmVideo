'''
Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, que é uma estrutura versátil e simples de entender.
Por exemplo:

for c in range(0, 4):

print(c)

print(‘Acabou’)

'''

'''
** Laços de repetição/iteração
    >>> Laços com variável de controle
            >>> laço c no intervalo(1,10)
                    passo
                pega
            
            >>> for c in range(1,10):
                    passo
                pega
    >>> Podemos colocar vários comandos dentro do laço for
          >>> laço c no intervalo(0,3)
                passo
                pula
              passo
              pega
          >>> for c in range(0,3):
                passo
                pula
              passo
              pega
    >>> Podemos colocar 'if' dentro do laço for
    >>> Podemos colocar 'for' dentro do laço for
    
*** Precisamos identar!

'''

#### Prática ####

#Nada prático!
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')


##############################################

for c in range(0, 6): # Não é contado o ÚLTIMO número
    print(c)
print('FIM') # Contado apenas 1 vez - fora do for

##############################################

for c in range(6, 0, -1): # Conta para trás
    print(c)

##############################################

for c in range(0, 7, 2): # Conta de 2 em 2
    print(c)
##############################################

n = int(input('Digite um número: '))

for c in range(0, n+1):
    print(c)
print('FIM')

##############################################

for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')

##############################################

s = 0

for c in range(0,10):
    n = int(input('Digite um valor: '))
    s = s + n # s += n
print('O somatório dos valores digitados é: {} '.format(s))

##############################################

inicio = int(input('Digite um valor: '))
fim = int(input('Digite um valor: '))
intevalo = int(input('Digite um valor: '))

for c in range(inicio, fim, intevalo):
    print(c)