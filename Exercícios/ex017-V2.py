#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacentede um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import hypot

n1 = float(input('Digite o comprimento do cateto oposto:'))
n2 = float(input('Digite o comprimento do cateto adjacente:'))
h = hypot(n1, n2)
print('A hipotenusa vai medir:{:.2f}'.format(h))
