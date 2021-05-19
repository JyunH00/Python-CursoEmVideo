'''
Exercício 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
'''

##### Resolução #####

cores = {'finaliza':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m'
         }

print('-=-'*30)
print('====APROVAÇÃO DE EMPRÉSTIMO====')
print('Escreva o {}VALOR DA CASA{}'.format(cores['azul'], cores['finaliza']))
print('Escreva seu {}SALÁRIO{}'.format(cores['amarelo'], cores['finaliza']))
print('Escreva em {}QUANTOS ANOS IRÁ PAGAR A CASA{} '.format(cores['vermelho'], cores['finaliza']))
print('\n{}A MENSALIDADE NÃO PODERÁ EXCEDER 30% DO SALÁRIO{}'.format(cores['vermelho'], cores['finaliza']))
print('-=-'*30)

### Criação das variáveis ###

valCasa = float(input('Escreva o {}VALOR DA CASA{}: R$ '.format(cores['azul'], cores['finaliza'])))
valSal = float(input('Escreva o {}VALOR DO SEU SALÁRIO{}: R$ '.format(cores['amarelo'], cores['finaliza'])))
qtdAnos = int(input('Escreva a {}QUANTIDADE DE ANOS{}: '.format(cores['vermelho'], cores['finaliza'])))

mensalidade = valCasa / (qtdAnos * 12)

if mensalidade <= (valSal * 0.3):
    print('\nO empréstimo foi {}ACEITO!{}'.format(cores['azul'], cores['finaliza']))
    print('O valor da mensalidade será de {}R${:.2f}{}'.format(cores['verde'], mensalidade, cores['finaliza']))
else:
    print('\n{}EMPRÉSTIMO NEGADO{}'.format(cores['vermelho'], cores['finaliza']))
    print('A mensalidade é de R${:.2f} e seu salário é de R${:.2f}, ultrapassando os 30%'.format(mensalidade,valSal))
