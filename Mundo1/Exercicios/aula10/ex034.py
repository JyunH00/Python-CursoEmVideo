'''
Exercício 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salário superiores a R$1.250.00, calcule um aumento de 10%.
Para os inferiores ou iguais o aumento é de 15%.
'''

##### Resolução #####

print('-=-'*30)
print('Calculador de aumento de salário.')
print('-=-'*30)

### Criação das variáveis ###

salario = float(input('Digite seu salário: '))

### Condições ###

if salario > 1250:
    salarioN = salario * 1.10
    print('O salário de R${:.2f} com um aumento de 10% é de R${:.2f}'.format(salario, salarioN))
else:
    salarioN = salario * 1.15
    print('O salário de R${:.2f} com um aumento de 15% é de R${:.2f}'.format(salario, salarioN))