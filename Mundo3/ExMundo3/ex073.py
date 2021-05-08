'''
Exercício 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela de Campeonato Brasileiro de Futebol. na
ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Fluminense;
'''

#### Resolução ####

#### Variáveis ####

times = ('Flamengo', 'Internacional', 'Atlético Mineiro', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos',
         'Athlético Paranaense', 'RB Bragantino', 'Ceará', 'Corinthians', 'Atlético Goianiense', 'Bahia', 'Sport Recife',
         'Fortaleza EC', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')

print('-=-'* 20)
print(f'Lista de times do Brasileirão: {times}')
print('-=-'* 20)
print(f'Os 5 primeiros são: {times[:5]}') # COMEÇA DO 0
print('-=-'* 20)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=-'* 20)
print(f'Lista de times do Brasileirão: {sorted(times)}')
print('-=-'* 20)
print('O time Fluminense está na {}º posição'.format(times.index('Fluminense') + 1)) # COMEÇA DO 0
print('-=-'* 20)

'''
para usar fstring utilize '' '' para strings.
'''