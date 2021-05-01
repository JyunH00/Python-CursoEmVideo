'''
Exercício 43: Desenvola uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

> Abaixo de 18.5: Abaixo do Peso
> Entre 18.5 e 25: Peso ideal
> 25 até 30: Sobrepeso
> 30 até 40: Obesidade
> Acima de 40: Obesidade mórbida
'''

##### Resolução #####

cores = {'finaliza':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'magenta':'\033[35m'
         }

print('-=-'*30)
print('====CALCULADOR DE IMC (ÍNDICE DE MASSA CORPÓREO)====')
print('\nDiga seu peso e direi seu IMC:')
print('''\n> Abaixo de 18.5: {}Abaixo do Peso{}\n
> Entre 18.5 e 25: {}Peso ideal{}\n
> 25 até 30: {}Sobrepeso{}\n
> 30 até 40: {}Obesidade{}\n
> Acima de 40: {}Obesidade mórbida{}\n
'''.format(cores['azul'], cores['finaliza'], cores['verde'], cores['finaliza'], cores['magenta'], cores['finaliza'], cores['amarelo'], cores['finaliza'], cores['vermelho'], cores['finaliza']  ))
print('-=-'*30)

### Criação das variáveis ###

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura * altura) # peso / (pow(altura, 2) , peso / (altura ** 2)


if imc < 18.5:
    print('Você tem o IMC de {:.2f} e sua categoria é {}Abaixo do peso{}.'.format(imc, cores['vermelho'], cores['finaliza']))
elif 18.5 <= imc < 25:
    print('Você tem o IMC de {:.2f} e sua categoria é {}Peso ideal{}.'.format(imc, cores['azul'], cores['finaliza'] ))
elif 25 <= imc < 30:
    print('Você tem o IMC de {:.2f} e sua categoria é {}Sobrepeso{}.'.format(imc, cores['amarelo'], cores['finaliza']))
elif 30 <= imc < 40:
    print('Você tem o IMC de {:.2f} e sua categoria é {}Obesidade{}.'.format(imc, cores['verde'], cores['finaliza']))
elif imc >= 40:
    print('Você tem o IMC de {:.2f} e sua categoria é {}Obesidade mórbida{}.'.format(imc, cores['magenta'], cores['finaliza']))