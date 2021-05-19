'''
Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python. Funções são trechos de
código que podem ser executados em momentos diferentes de nossos códigos em Python. Veja como funciona o comando def em
Python e como utilizá-lo com parâmetros simples e múltiplos.
'''

'''
** FUNÇÕES
    >>> Rotina
    >>> Algumas funções já vem com o python!
            >>> print(), len(), input(), int(), float(), ...
    >>> Podemos criar nossas próprias funções para satisfazer nossas necessidades.
    >>> utlizamos o nome def ??():
        >>> podemos utilzar parâmetros -> colocamos dentro dos parênteses.
        >>> podemos empacotar os parâmetros (tamanho variável de parâmetros) -> def ?? (* ??)
'''

#### Prática ####

# Repetindo muito os comandos
a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

print()
# Podemos utilizar as funções!
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
# é necessário pular 2 linhas entre as funções e/ou o programa principal!


#Programa Principal
soma(4, 5)
soma(a=8, b=9)
soma(b=2, a=1)

print()
#######################################################################
def contador(* num):
    """
    -> Essa função imprime todos os valores colocados no parâmetro e mostra quantos valores foram impressos
    :param num: Parâmetros variáveis de números inteiros
    :return: Não retorna valor
    """
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

print()
#######################################################################
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

