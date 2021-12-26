#Escreva um programa que converta uma temperatura digita em °C e converta para °F

c = float(input('Digite a temperatura em °C:'))
f = ((9*c/5)+32)
print('A temperatura de {}°C corresponde à {} °F'.format(c, f))