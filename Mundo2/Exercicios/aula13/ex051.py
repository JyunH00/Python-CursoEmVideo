'''
Exercício 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa prgressão
'''


### Resolução ###

print('-=-'*50)
print('Este programa irá mostrar os 10 primeiros termos de uma PA. Você irá fornecer o primeiro termo e a razão')
print('-=-'*50)

### Criação das variáveis ###

pTermo = int(input('Digite um número inteiro: '))

razao = int(input('Digite a razão da PA: ')) # Razão da PA

### Laço ###

atual = pTermo # Resultado dos termos -> Começamos com o primeiro resultado = primeiro termo
for c in range(0,10):
    print('{:2}º: {:2}'.format(c + 1, atual))
    atual += razao # Atualização do resultado dos termos
