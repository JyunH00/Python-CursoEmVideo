'''
Exercício 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o
número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não tela o
processo de cálculo do fatorial
'''

# Resolução #

# Funções #

def fatorial(valor, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param valor: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """

    fatN = 1
    for i in range(valor, 0, -1):
        fatN *= i
        if show == True:
            if i == 1:
                print(f'{i} = ', end='')
            else:
                print(f'{i} X ', end='')
    return fatN


#Programa principal

print(fatorial(50,show=True))

help(fatorial)