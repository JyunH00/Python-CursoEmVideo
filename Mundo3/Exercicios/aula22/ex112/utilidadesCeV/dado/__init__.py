'''
Exercício 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função
chamada leiaDinheiro() que seja capaz de funcionar como a função input() mas com uma validação de dados para aceitar
apenas valores que sejam monetários
'''

# Resolução #

# Funções #

def leiaDinheiro(str):

    while True:
        print(str, end='')
        n = input('').strip().replace(',', '.')
        if n == '' or n.isalpha():
            print(f'\033[31m "{n}" é um preço inválido! \033[m')
        else:
            break
    return float(n)