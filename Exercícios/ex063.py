'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos da uma
sequência de Fibonacci'''

num1 = int(input('Digite um número:'))
elementos = int(input('Digite quantos elementos da sequência você quer:'))
num2 = 1
iniciofim = 0

while iniciofim != elementos:
    soma = num1 + num2
    print('{} + {} = {}'.format(num1, num2, soma))
    num2 = num1
    num1 = soma
    iniciofim = iniciofim + 1
