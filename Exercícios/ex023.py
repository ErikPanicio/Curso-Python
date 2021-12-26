'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
Ex: Digite um número:1834
Unidade:4 ; Dezena:3 ; Centena:8 ; Milhar:1'''

numero = str(input('Digite um número de 0 a 9999:')).strip()
print('Milhar:{}, Centena:{}, Dezena:{}, Unidade:{}'.format(numero[0], numero[1], numero[2], numero[3]))
