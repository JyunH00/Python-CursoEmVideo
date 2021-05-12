'''
Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python. Os dicionários são variáveis
compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.
'''

'''
** Variáveis compostas
    >>> tuplas, listas, DICIONÁRIOS
        >>> Não podemos atribuir múltiplos valores em variáveis simples
        >>> lanche = 'hamburguer'
        >>> lanche = 'suco' -> lanche vira 'suco'

** Dicionários
    >>> Conseguimos personalizar os índices (Como índices literais!)
    >>> Utilizamos {}, dict()
    
    >>> dados = dict() ou dados = {}
        dados = {'nome': 'Pedro', 'idade': 25}
        print(dados['nome']) -> Pedro
        print(dados['idade']) -> 25
    * Não temos append em dicionários!
        >>> dados['sexo'] = 'M'

* Alguns comandos:
    >>> del dados['idade']
    >>> filme = { 'titulo': 'Star Wars,
                'ano': 1977,
                'diretor': 'George Lucas'
                }
    >>> print(filme.values()) -> Retorna todos os  valores de filme ('Star Wars', etc)
    >>> print(filme.keys()) -> Retorna as chaves de filme (titulo, ano, etc)
    >>> print(filme.items()) -> Retorna todos os valores e chaves.
    
    >>> for k,v in filme.items():
            print(f'O {k} é {v}')

*** Podemos colocar dicionários em listas!
'''

#### Prática ####

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

print(pessoas)

print(pessoas['nome'])

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for k in pessoas.values():
    print(k)

del pessoas['sexo']

pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5

for k, v in pessoas.items(): # Equivale ao enumerate!
    print(f'{k} = {v}')

print()
###########################################################################
'''
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1])
print(brasil[1]['sigla'])
'''
print()
###########################################################################

estado = dict()
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
    print()