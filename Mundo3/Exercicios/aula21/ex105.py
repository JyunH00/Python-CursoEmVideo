'''
Exercício 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função
'''

# Resolução #

# Funções #

def notas(* notas, sit=False):
    """
    -> Função para analisar notas e situaçãoes de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    somaM = media = 0
    for i in notas:
        somaM += i
    media = somaM/ len(notas)

    dictNotas = {'total': len(notas),
                 'maior': max(notas),
                 'menor': min(notas),
                 'média': media}

    situacao = ''
    if media >= 7:
        situacao = 'BOA'
    elif 6 <= media <= 7:
        situacao = 'RAZOÁVEL'
    else:
        situacao = 'RUIM'

    if sit == True:
        dictNotas['situação'] = situacao

    return dictNotas

#Programa Principal

resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)

'''
Solução um pouco diferente no vídeo!
*** Podemos usar sum(notas) para somar todos os valores da tupla!
'''