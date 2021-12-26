#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

print('Vou dizer se o número é Par ou Ímpar!')
numero = int(input('\nDigite o número:'))
par_ou_impar = numero % 2
if par_ou_impar == 0:
    print('{} é\033[34m Par\033[m'.format(numero))
else:
    print('{} é\033[34m Ímpar\033[m'.format(numero))