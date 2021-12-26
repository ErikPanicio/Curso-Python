'''Faça um programa que leia um número inteiro e diga se ele é ou não é um número primo'''

num = int(input('Digite um número:'))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont = cont + 1     #Se o número (num) for divísivel pelo valor de c adiciona +1 para o contador. Então se o número for primo ele será divísivel duas vezes pelo c (divísivel por 1 e por ele mesmo).
if cont == 2:               #Quantas vezes o número foi divísivel por c, caso seja primo será divido apenas duas vezes.
    print('O número {} é primo!'.format(num))
elif cont > 2 or cont < 2:  #Caso seja divísivel apenas por um número ou seja divísivel por mais de dois números, não será primo.
    print('O número {} não é primo!'.format(num))
