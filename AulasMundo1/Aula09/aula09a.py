'''
Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento
de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(),
strip(), junção com join().
'''

'''
Para criar uma string utilizamos '' ou ""

>>> frase = 'Curso em Vídeo Python'

** Fatiamento : Conseguir pegar uma letra ou um intervalo de letras da String
    >>>frase[númeroIndice]
    >>>frase[númeroIndice:númeroIndice]
    >>>frase[númeroIndice:númeroIndice:númeroDePulos]
    >>>frase[:númeroIndice] -> começa do caractere 0 == frase[0:número]
    >>>frase[númeroIndice:] -> vai até do número até o final da String
    >>>frase[númeroIndice::númeroDePulos] -> Vai do número até o final, pulando o número de pulos
    
** Análise: Consegui obter algumas informações sobre a String
    >>>len(frase) -> comprimento da frase
    >>>frase.count('caractere') -> contar quantas vezes aparece o caractere escolhido
    >>>frase.count('caractere', númeroIndice, númeroIndice) -> contar quantas vezes aparece o caractere escolhido no 
                                                               intervalo escolhido (análise e fatiamento)
    >>>frase.find('parteString') -> Fala em que posição começou a parte da String
        >>> Retorna o valor -1 caso não exista a parte String passada.
    >>> 'String' in frase -> Diz se existe ou não a string na frase
        >>> True ou False
        
** Transformação
    >>> frase.replace('String, outraString') -> Substitui parte da String por outra
    >>> frase.upper() -> Maiúscula
    >>> frase.lower() -> Minúscula
    >>> frase.capitalize() -> Joga todos os caracteres para minúscula e o primeiro caractere em maiúsculo
    >>> frase.title() -> Transforma cada palavra com a primeira letra em maiúscula.
    >>> frase.strip() -> Remove os espaços excedentes das extremidades
        >>> frase.rstrip() -> Remove os espaços excedentes da direita
        >>> frase.lstrip() -> Remove os espaços excedentes da esquerda
        
** Divisão
    >>> frase.split() -> Ocorre uma divisão em cada espaço (Criando uma nova lista para cada palavra)
    
** Junção
    >>> '-'.join(frase) -> Juntar todos os elementos de 'frase' com '-'
'''

'''
*** TODA STRING É IMUTÁVEL
*** Lembrar dos comandos 'r...' ou 'l...'
'''

#### Prática ####

frase = 'Curso em Vídeo Python'
dividido = frase.split()

#Testes com a string 'frase'
print(len(frase))
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.lower().find('Vídeo'))
print(frase.split())
print(dividido[0])
print(dividido[2][3])

#Escrever uma frase grande utilize """ """
print("""Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento
de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(),
strip(), junção com join().""")

