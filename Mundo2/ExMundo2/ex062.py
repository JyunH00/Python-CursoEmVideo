'''
Exercício 62: Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
encerra quando ele disse que quer mostrar 0 termos.
'''

#### Resolução ####


print('-=-'*20)
print('PA DE N TERMOS')
print('-=-'*20)

### Variáveis ###

pTermo = int(input('Digite o primeiro termo da PA: \n'))

razao = int(input('Digite a razão da PA: \n'))

atual = pTermo

# Laço While #
ntermos = 0
while ntermos != 10:
    print('{}º: {}'.format(ntermos + 1, atual))
    atual += razao
    ntermos += 1

adTermos = int(input('\nGostaria de adicionar mais termos na PA? Se sim, digite o número! \n '))

while adTermos != 0:
    for i in range((ntermos + 1), (ntermos + adTermos + 1)):
        print('{}º: {}'.format(ntermos + 1, atual))
        atual += razao
        ntermos += 1
    adTermos = int(input('\nGostaria de adicionar mais termos na PA? Se sim, digite o número! \n '))

'''
Podemos usar laços aninhados! Veja o vídeo do desafio 62.
'''