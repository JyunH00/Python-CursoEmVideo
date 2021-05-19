'''
Exercício 113: Reescreva a função leiaInt() que fizemos no desafio 104. Incluindo agora a possibilidade da digitação de
um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''

# Resolução #

# Funções #

def leiaInt(str):
    while True:
        try:
            print(str, end='')
            n = int(input(''))
        except:
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')

        else:
            break
    return n

def leiaFloat(str):
    while True:
        try:
            print(str, end='')
            n = float(input(''))
            break
        except:
            print('\033[31mERRO! Digite um número real válido!\033[m')
        else:
            break
    return n

#Programa principal

inteiro = leiaInt('Digite um Inteiro: ')

real = leiaFloat('Digite um Real: ')

print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')

'''
Solução do vídeo um pouco diferente!
'''