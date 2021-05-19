'''
Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo como criar módulos em Python e reutilizar
nossos códigos em outros projetos. Vamos aprender também como agrupar vários módulos em um pacote, ampliando ainda mais
a modularização em grandes projetos em Python.
'''

'''
** Modularização
    >>> Surgiu no inícido da década de 60
    >>> Sistemas ficando cada vez maiores
    >>> Foco: Dividir um programa grande
    >>> Foco: Aumentar a legibilidade
    >>> Foco: Facilitar a manutenção
    
* Vantagens
    >>> Organização do código
    >>> Facilidade na manutenção
    >>> Ocultação de código detalhado
    >>> Reutilização em outros projetos
    
** Pacotes
    >>> Pasta que contém módulos
    >>> Separar por assuntos
    >>> import ???
    >>> from ??? import ???
    >>> Cada pasta deve conter __init__.py
'''

#### Prática #####

from uteis import numeros

#from uteis import fatorial, dobro

num = int(input('Digite um valor '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')