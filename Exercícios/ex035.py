#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se ela podem ou não formar um triângulo

reta1 = float(input('Digite a primeira reta:'))
reta2 = float(input('Digite a segunda reta:'))
reta3 = float(input('Digite a teceira reta:'))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Esses segmentos\033[1;32m podem\033[m formar um triângulo!')
else:
    print('Os segmentos\033[1;31m não podem\033[m formar um triângulo!')