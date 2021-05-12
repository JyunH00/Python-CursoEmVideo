'''
Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que
permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
'''

'''
** Variáveis compostas
    >>> tuplas, LISTAS, dicionários
    >>> Não podemos atribuir múltiplos valores em variáveis simples
        >>> lanche = 'hamburguer'
        >>> lanche = 'suco' -> lanche vira 'suco'
        
** Listas
    >>> Utilizamos [], list
    >>> Variável que guarda vários valores
    >>> Itens identificados por índices (0 -> ?)
    >>> LISTAS SÂO MUTÁVEIS (Podem ser modificadas)
    
* Alguns comandos:
    >>> lista.append(?) -> Adiciona um item no final da lista (Se for um str, colocamos '').
    >>> lista.insert(0, ?) -> Adiciona um item no índice indicado (Se for um str, colocamos '').
    >>> del lista[?] -> Remove um item pelo índice.
    >>> lista.pop(?) -> Remove um item pelo índice, se não colocar índice, ele removerá o último.
    >>> lista.remove(?) -> Remove um item pelo valor (Se for um str, colocamos '').
    >>> if ? in lista:
            lista.remove(?) -> Apenas remove se houver o item na lista
    >>> ??.sort() -> Deixa em ordem crescente
    >>> ??.sort(reverse = True) -> Deixa em ordem decrescente
    >>> len(valores) -> Tamanho da lista
    >>> ?? = list((range(4, 11)) -> Cria uma lista de 4 a 10 em ordem.
    >>> ?? = [8, 2 , 5, 4, 9, 3, 0]
        
'''

#### Prática ####

#num = (2, 5, 9, 1)
#num[2] = 3 - > Erro
#print(num)

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse = True)
num.insert(2,2)
num.remove(2) # Elimina a primeira ocorrência

if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')

num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')

######################################################

valores = [] # valores = list()
#valores.append(5)
#valores.append(9)
#valores.append(4)

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei {v}!')
print('Cheguei ao final da lista')

######################################################

a = [2, 3, 4, 7]
#b = a  # Não é uma cópia! (Cria uma ligação!)
b = a[:] # Cria uma cópia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')