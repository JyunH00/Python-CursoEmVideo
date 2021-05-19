'''
Exercício 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:

> À vista dinheiro/cheque: 10% de desconto
> À vista no cartão: 5% de desconto
> 2x no cartão: Preço normal
> 3x ou mais no cartão: 20% de juros
'''

##### Resolução #####

cores = {'finaliza':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'magenta':'\033[35m'
         }


print('====VALOR DE PAGAMENTO PARA CADA TIPO====')


### Criação das variáveis ###

valorP = float(input('\nDigite o valor do produto: R$ '))

print('\nDiga seu  tipo de pagamento:')

print('''\n> [1] À vista dinheiro/cheque: {}10% de desconto{}\n
> [2] À vista no cartão: {}5% de desconto{}\n
> [3] 2x no cartão: {}Preço normal{}\n
> [4] 3x ou mais no cartão: {}20% de juros{}
'''.format(cores['azul'], cores['finaliza'], cores['verde'], cores['finaliza'], cores['magenta'], cores['finaliza'], cores['amarelo'], cores['finaliza']))

opPag = int(input('Digite a opção de pagamento (1 - 4): '))

#### Condições ####

if 1 <= opPag <= 4:
    if opPag == 1:
        vista = valorP * 0.90
        print('Sua compra terá 10% de desconto')
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valorP, vista))
    elif opPag == 2:
        vistaC = valorP * 0.95
        print('Sua compra terá 5% de desconto')
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valorP, vistaC))
    elif opPag == 3:
        print('Sua compra terá o preço normal')
        print('Sua com pra vai custar R${:.2f}'.format(valorP))
    elif opPag == 4:
        parcelas = int(input('Quantas parcelas? '))

        if parcelas >= 3:
            valorPar = (valorP / parcelas) * 1.2
            valorParT = valorPar * parcelas
            print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, valorPar))
            print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valorP, valorParT))
        else:
            print('{}Coloque parcelas de 3x ou mais nessa opção!{}'.format(cores['vermelho'], cores['finaliza']))
else:
    print('{}COLOQUE UMA OPÇÃO VÁLIDA!{}'.format(cores['vermelho'], cores['finaliza']))

'''
OBSERVAÇÕES: Não é necessário colocar o primeiro if/else

'''