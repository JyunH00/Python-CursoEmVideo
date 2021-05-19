'''
Exercício 92: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
dicionário se po acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (35 anos de contribuição)
'''

# Resolução #

from datetime import date

# Variáveis #

infoP = {'nome': str(input('Nome: ')),
         'idade': date.today().year - int(input('Ano de Nascimento: ')),
         'ctps': int(input('Carteira de Trabalho (0 não tem): ')),
         }

# Caso ctps for diferente de 0
if infoP['ctps'] != 0:
    infoP['contratação'] = int(input('Ano de contratação: '))
    infoP['salário'] = float(input('Salário: R$  '))
    infoP['aposentadoria'] = (infoP['contratação'] + 35 - date.today().year) + infoP['idade']


# Prints #
print('-='*30)
for k, v in infoP.items():
    print(f'- {k} tem o valor de {v}.')


