cores = {'finaliza':'\033[m',
         'azul':'\033[1;34m',
         'amarelo':'\033[1;33m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'magenta':'\033[1;35m'
         }


from time import sleep

def leiaInt(str):
    while True:
        try:
            print(str, end='')
            n = int(input(''))
        except:
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')

        else:
            break
    return n

def cabeçalho(txt):
    print('\033[1m-\033[m' * 30)
    print(f'\033[1m{txt}\033[m'.center(35))
    print('\033[1m-\033[m' * 30)


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'{cores["amarelo"]}{c}{cores["finaliza"]} - {cores["azul"]}{i}{cores["finaliza"]}')
        c += 1
    print('\033[1m-\033[m' * 30)
    opc = leiaInt(f'{cores["amarelo"]}Sua Opção:{cores["finaliza"]} ')
    return opc
