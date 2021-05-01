'''
Exercício 40: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

> Média abaixo de 5.0: REPROVADO
> Média entre 5.0 e 6.9: RECUPERAÇÃO
> Média 7.0 ou superior: APROVADO
'''

##### Resolução #####

cores = {'finaliza':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m'
         }

print('-=-'*30)
print('====CALCULADOR DE MÉDIA DE ALUNO====')
print('Coloque suas notas para saber se foi REPROVADO, RECUPERAÇÃO ou APROVADO')
print('''> Média abaixo de 5.0: {}REPROVADO{}
\n> Média entre 5.0 e 6.9: {}RECUPERAÇÃO{}
\n> Média 7.0 ou superior: {}APROVADO{}
'''.format(cores['vermelho'], cores['finaliza'], cores['amarelo'], cores['finaliza'], cores['azul'], cores['finaliza']))
print('-=-'*30)

### Criação das variáveis ###

nota1 = float(input('Coloque sua primeira nota: '))
nota2 = float(input('Coloque sua segunda nota: '))

media = (nota1 + nota2) / 2

### Condições ###

if media < 5:
    print('Você está {}REPROVADO{} com uma média de {}{:.1f}{}.'.format(cores['vermelho'], cores['finaliza'], cores['vermelho'], media, cores['finaliza'] ))
elif 5 <= media < 7:
    print('Você está em {}RECUPERAÇÂO{} com uma média de {}{:.1f}{}.'.format(cores['amarelo'], cores['finaliza'], cores['amarelo'],media, cores['finaliza'], ))
elif 7 <= media < 10:
    print('Você está {}APROVADO{} com uma média de {}{:.1f}{}.'.format(cores['azul'], cores['finaliza'], cores['azul'], media, cores['finaliza'], ))