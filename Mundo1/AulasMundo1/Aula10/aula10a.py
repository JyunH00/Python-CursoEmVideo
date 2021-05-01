'''
Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.
'''

'''
>>> Condições

** Estrutura sequencial
    >>> Comando seguidos sequencialmente sem condições

*** Condições
    >>> Representação estruturada/identada
    >>> Bloco Verdadeiro/Bloco Falso
    >>> Utilização:
        >>> if condição: bloco True
        >>> else: bloco False
    >>> Estrutura simples: apenas if
    >>> Estrutura composta: if e else
    
tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
    
print('--FIM--')

*** Condição simplificada

tempo = int(input('Quantos anos tem seu carro? '))

print('Carro novo' if tempo <= 3 else 'Carro velho')

print('--FIM--')
'''

#### Prática ####

# Condição Composta

nome = str(input('Qual é seu nome? '))

if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')

print('Bom dia, {}!'.format(nome))

############################################

# Condição Composta

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

print('A sua média foi {:.1f}'.format(m))

if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

# Condição Simplificada

print('PARABÈNS' if m >= 6.0 else 'ESTUDE MAIS!')