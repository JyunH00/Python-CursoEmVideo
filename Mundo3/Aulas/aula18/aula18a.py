'''
Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que
permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
'''

'''
** Listas (PARTE 2)

>>> dados = list()
    >>> dados.append('Pedro')
    >>> dados.append(25)

>>> pessoas = list()
    >>> pessoass.append(dados[:]) ( Append em estruturas!) -> [:] (cópia)
** Listas de listas!

>>> pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]] (Listas compostas/listas de listas)
    >>> print(pessoas[0][0]) -> Pedro
    >>> print(pessoas[1][1]) -> 19
    >>> print(pessoas[2][0]) -> João
    >>> print(pessoas[1]) -> ['Maria', 19] 
'''

#### Prática ####

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
# galera.append(teste) # Cria uma ligação entre as estururas! Se mudarmos teste, mudamos galera
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

##############################################################################

pessoas = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(pessoas)
print(pessoas[0][0])
print(pessoas[2][1])

for p in pessoas:
    print(p)
    print(f'{p[0]} tem {p[1]} anos de idade.')


##############################################################################

galera = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() # Limpa a lista dado
print(galera)
print(dado)

totmai = totmen = 0
for p in galera:
    if p[1] >=21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade')