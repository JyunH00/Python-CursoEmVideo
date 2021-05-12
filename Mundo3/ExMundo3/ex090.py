'''
Exercício 90: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final
mostre o conteúdo da estrutura na tela.

** 7.0 ou mais aprovado
'''

# Resolução #

# Variáveis #

aluno = {}

# Atribuindo os valores no dicionário
aluno['nome'] = str(input('Nome: '))
aluno['mediaNotas'] = float(input(f'Média de {aluno["nome"]}: '))

# Prints
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["mediaNotas"]}')

# Validando aprovação
if aluno["mediaNotas"] >= 7.0:
    aluno['situação'] = 'APROVADO'
    print(f'Situação é igual a {aluno["situação"]}')
else:
    aluno['situação'] = 'REPROVADO'
    print(f'Situação é igual a {aluno["situação"]}')


'''
Solução um pouco diferente no vídeo!
'''