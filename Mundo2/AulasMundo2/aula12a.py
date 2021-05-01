'''
Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif..
else em programas Python.
'''


'''
*** Condições Aninhadas
    >>> Estrutura condicional dentro de estrutura condicional
    >>> 'Se', 'senão se', 'senão'
    >>> 'if:', 'elif:', 'else:'
    >>> Podemos ter quantos elif quisermos
        >>> É necessário um if para existir elif
        >>> 'else' é opcional

>>> Usamos 'and' e 'or' para várias condições.
>>> Podemos usar 'in' como no exemplo abaixo para opções de uso

'''

#### Prática ####

nome = str(input('Qual seu nome? '))

if nome == 'Gustavo':
    print('QUe nome bonito!')
elif nome in 'Pedro Maria Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))