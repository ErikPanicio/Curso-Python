#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira

from math import floor

n = float(input('Digite um número qualquer:'))
print('O número {} tem a parte inteira:{}'.format(n, floor(n)))

