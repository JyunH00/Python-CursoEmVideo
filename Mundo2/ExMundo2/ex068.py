'''
Exercício 68: Faça um programa que jogue par ou ímpar com o jogador. O jogo só será interrompido quando o jogador PERDER.
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

#### Resolução ###

print('-=-'*20)
print('JOGO DO PAR OU ÍMPAR')
print('-=-'*20)

from random import  randint

### Variáveis ###

numJogador = contador = soma = 0
numComputador = randint(0, 10)
parImpar = ''

### Laço while ###

while True:
    soma = numJogador + numComputador

    numJogador = int(input('Digite um valor de 0 a 10: '))
    while numJogador < 0 or numJogador > 10:
        numJogador = int(input('Digite um valor de 0 a 10: '))

    parImpar = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
    while parImpar not in 'PI':
        parImpar = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]

    print('-=-' * 20)
    if parImpar == 'P' and (soma % 2) == 0:
        contador += 1
        print('--' * 20)
        print(f'Você jogou {numJogador} e o computador {numComputador}. Total de {soma} DEU PAR')
        print('--' * 20)
        print('Você VENCEU!')
        print('-=-' * 20)
        print('Vamos jogar novamente...')
    elif parImpar == 'I' and (soma % 2) == 0:
        print('--' * 20)
        print(f'Você jogou {numJogador} e o computador {numComputador}. Total de {soma} DEU PAR')
        print('--' * 20)
        print('Você PERDEU!')
        print('-=-' * 20)
        print(f'GAME OVER! Você venceu {contador} vezes.')
        break
    elif parImpar == 'P' and (soma % 2) != 0:
        print('--' * 20)
        print(f'Você jogou {numJogador} e o computador {numComputador}. Total de {soma} DEU ÍMPAR')
        print('--' * 20)
        print('Você PERDEU!')
        print('-=-' * 20)
        print(f'GAME OVER! Você venceu {contador} vezes.')
        break
    elif parImpar == 'I' and (soma % 2) != 0:
        contador += 1
        print('--' * 20)
        print(f'Você jogou {numJogador} e o computador {numComputador}. Total de {soma} DEU ÍMPAR')
        print('--' * 20)
        print('Você VENCEU!')
        print('-=-' * 20)
        print('Vamos jogar novamente...')

'''
Resolução um pouco diferente no vídeo!
'''