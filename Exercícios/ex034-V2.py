'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00
calcule um aumento de 10%. Para os inferiores ou iguais,o aumento é de 15%'''

salario = float(input('Digite o seu salário:R$'))
if salario > 1250:      #<---Estrutura Composta
    print('Seu salário com \033[1;30m10%\033[m de aumento é:\033[1;32mR${:.2f}\033[m'.format(salario+(salario/100*10)))
else:                   #<---Estrutura Composta
    print('Seu salário com \033[1;30m15%\033[m de aumento é:\033[1;32mR${:.2f}\033[m'.format(salario+(salario/100*15)))
