'''
Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python, o uso
de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python, escopo de
variáveis e retorno de resultados.
'''

'''
** Funções Parte II
    >>> Interactive Help
    >>> docstrings
    >>> Argumentos opcionais
    >>> Escopo de variáveis
    >>> Retorno de resultados

** Interactive Help
    >>> help()
    >>> Podemos chamar o Python Console e escrever help()
        >>> Escrevendo o nome das funções, bibliotecas, etc, temos todas as informações sobre os mesmos
    >>> Podemos escrever help(???) no código.
    >>> Podemos escrever print(???.__doc__)
    
** DOCSTRINGS
    >>> def contador(i, f, p):
            """ -> DOCSTRING
            -> Faz uma contagem e mostra na tela.
            : param i: início da contagem
            :param f: fim da contagem
            :param p: passo da contagem
            :return: sem retorno
            """ -> DOCSTRING
            c = i
            while c <= f:
                print(f'{c}, end='..')
            c += p
        print('FIM!')
        
        contador(2, 10, 2)
        help(contador) 
    >>> Podemos descrever nossas funcionalidades utlizando docstring!
    
** Parâmetros Opcionais
    >>> def somar(a=0, b=0, c=0): -> parâmetros opcionais! Colocamos um valor padrão para os parâmetros.
            s = a + b + c
            print(f'A soma vale {s}')
            
        somar(3, 2, 5)
        somar(8, 4)
        somar()
  
** Escopo de variáveis
    >>> def teste():
            x = 8
            print(f'{n})
        
        #Programa principal
            n = 3
            print(f'{n})
            teste()
            print(f'{x}') -> ERRO
    
    >>> n é variável global/possui escopo global
    >>> x é variável local/possui escopo local
    
    >>> global ?? -> Colocamos dentro de uma função para a variável ?? ser global

** Retornando valores
    >>> return
    >>> def somar(a=0, b=0, c=0):
            s = a + b + c
            #print(f'A soma vale {s})
            return s
        
        r1 = somar(3,2,5)
        r2 = soma(2,2)
        r3 = soma(6)
          
    >>> Com return. podemos ter personalização dos resultados
'''

#### Prática ####

# Conceitos gerais!
def fatorial(num = 1): # -> Parâmetro opcional!
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3} ')


############################################################

# Return não se limita a valores inteiros!
def par(n = 0): # -> Parâmetro opcional!
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')

#############################################################

#Interactive help
help(print)
print(print.__doc__)

#############################################################

#DocStrings
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    : param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
        print('FIM!')

contador(2, 10, 2)
help(contador)