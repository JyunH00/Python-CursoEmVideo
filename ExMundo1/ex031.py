'''
Exercício 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0.50 por km para viagens de até 200km e R$0.45 para viagens mais longas.
'''

##### Resolução #####

print('-=-'*50)
print('Olá, seja bem-vindo(a) ao calculador de preço de passagens!')
print('Nosso cálculo é simples: Se sua viagem for de até 200km, iremos cobrar R$0.50 por km. E para viagens mais longas R$0.45 por km.')
print('-=-'*50)

### Criação das variáveis ###

distancia = float(input('Qual a distância da sua viagem? '))

### Condições ###

if distancia <= 200:
    preco = distancia * 0.5
    print('Sua viagem de {:.1f}km custará R${:.2f}'.format(distancia, preco))
else:
    preco = distancia * 0.45
    print('Sua viagem de {:.1f}km custará R${:.2f}'.format(distancia,preco))

'''
Outra resolução

>>> condição simplificada

preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
'''