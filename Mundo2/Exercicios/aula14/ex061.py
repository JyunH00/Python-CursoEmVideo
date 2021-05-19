'''
Exercício 61: Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
progrssão usando a estrutura while.
'''

#### Resolução ####


print('-=-'*20)
print('PA DE 10 TERMOS')
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
