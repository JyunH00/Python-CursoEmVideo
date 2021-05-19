'''
Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções. Aprenda como usar a
estrutura try except no Python de uma forma simples.
'''

'''
** Exceção
    >>> Ocorre quando há um erro que não é sintático.
    >>> ValueError
    >>> NameError
    >>> ZeroDivision Error
    >>> TypeError
    >>> IndexError
    >>> KeyError
    >>> ModuleNotFoundError
    ...
    
** try:
        operação
   except:
        falhou
        continue (opcional)
   else: (opcional)
        deu certo
   finally: (opcional) -> Ocorre em qualquer ocasião
        certo/falha

'''

#### Prática ####
'''
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
'''
#######################################################

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou!')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')