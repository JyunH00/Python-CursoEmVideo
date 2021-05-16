'''
Exercício 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input do
Python, só que fazendo a validação para aceitar apenas um valor numérico.

Ex:
n = leiaInt('Digite um n')
'''

# Resolução #

# Funções #

def leiaInt(str):
    while True:
        print(str, end='')
        n = input('')
        if n == '' or n.isnumeric() == False:
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
        else:
            break
    return n


#Programa Principal

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')

'''
Solução do vídeo um pouco diferente!
'''