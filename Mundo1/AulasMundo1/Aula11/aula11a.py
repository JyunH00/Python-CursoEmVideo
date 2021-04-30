'''
Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus
programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades.
'''

'''
** Código ANSI
    >>> \033[style; text; background m
        >>> Os 3 tipos são opcionais e podem ser colocados em qualquer ordem

** Style
    >>> 0, 1, 4, 7
        >>> 0: None
        >>> 1: Negrito
        >>> 4: Sublinhado
        >>> 7: Negative (Inverter)

** Text
    >>> 30 --> 37
        >>> 30: Branco
        >>> 31: Vermelho
        >>> 32: Verde
        >>> 33: Amarelo
        >>> 34: Azul
        >>> 35: Magenta
        >>> 36: Ciano
        >>> 37: CInza (Padrão)
        
*** Background
    >>> 40 --> 47
        (Mesmas cores do texto)

'''

#### Prática #####

print('\033[1;31;43mOlá, mundo!\033[m')

print('\033[7;30mOlá, mundo!\033[m')

print('\033[0;33;44mOlá, mundo!\033[m')

print('\033[7;33;44mOlá, mundo!\033[m')

a = 3
b = 5

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))

#################################################################

nome = 'Gustavo'

cores = {'Limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, '\033[m'))