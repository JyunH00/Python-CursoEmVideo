'''
Exercício 58: Melhore o deafio 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

#### Resolução ####

from random import randint

from time import sleep # Resolução do víd

print('-=-'*20)
print('Estou pensando em um número entre 0 e 10...')
print('Adivinhe!')
print('-=-'*20)

numComputador = randint(0,10)

numPessoa = int(input('Digite o número em que estou pensando! \n'))

numTentativas = 1
while numPessoa != numComputador:

    print('PROCESSANDO...')
    sleep(1)  # Fica 1 segundos "processando"
    numPessoa = int(input('Poxa, tente de novo! \n'))
    numTentativas += 1

print('Caramba! Você acertou! O número que eu pensei era mesmo o {}. Você acertou na {}º tentativa!'.format(numComputador, numTentativas))

'''
>>> Uso de bool!

acertou = False
while not acertou...
'''