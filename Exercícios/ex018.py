#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,cosseno e tangente desse ângulo

from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo:'))
seno = sin(radians(ang))
cosseno = cos((radians(ang)))
tangente = tan(radians((ang)))
print('O ângulo de {} tem o seno de {:.2f} o cosseno de {:.2f} e a tangente de {:.2f}'.format(ang, seno, cosseno, tangente))
