'''
Exercício 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''


### Resolução ###

cores = {'finaliza':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'magenta':'\033[35m'
         }

print('-=-'*30)
print('Coloque um número inteiro e direi se ele é primo ou não!')
print('-=-'*30)

### Criação de Variáveis ###

numInt = int(input('Digite um número inteiro: '))

# Casos especiais #

if numInt < 0:
    print('{}O número {} é negativo! Números negativos não podem ser primos!{}'.format(cores['vermelho'], numInt, cores['finaliza']))
elif numInt == 0:
    print('{}O número 0 não pode ser um número primo, pois não podemos dividí-lo por ele mesmo! 0/0 é indeterminado!{}'.format(cores['vermelho'], cores['finaliza']))
elif numInt == 1:
    print('{}O número 1 não pode ser número primo, pois ele só é dividido por ele mesmo!{}'.format(cores['vermelho'], cores['finaliza']))
elif numInt == 2:
    print('{}O número 2 é o único número par primo!{}'.format(cores['azul'], cores['finaliza']))

# Caso geral #

verificaP = False # Verificador de primo

for c in range(2, numInt): # laço que vai de 2 até número - 1
    if numInt % c == 0: # Verifica se tem resto 0
        print('{}O número não é primo!{}.'.format(cores['vermelho'], cores['finaliza']))
        verificaP = False
        break # Se o número não for primo, ele imediatamente para o laço
    else:
        verificaP = True

if verificaP == True: # Se nenhum dos números a partir de 2 até o (número esolhido - 1), divididos pelo número escolhido não derem resto 0, o número é primo.
    print('{}O número é primo!{}'.format(cores['azul'], cores['finaliza']))


'''
*** VER O VìDEO -> Solução bem diferente!
'''