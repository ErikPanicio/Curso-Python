#Faça um programa que leia três números e mostre qual é o maior e qual é o menor

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))
# Definindo o maior número
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
# Definindo o menor número
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O maior número é:\033[1;30m{}\033[m'.format(maior))
print('O menor número é:\033[1;30m{}\033[m'.format(menor))