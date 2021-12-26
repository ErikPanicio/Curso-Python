#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

ano = int(input('Digite o ano:'))
ano_bissexto = ano % 4                  #Está errado pois dividirá o ano pode 4 para achar o valor 0 de cada quatro números como o ano bissexto é (quatro em cada quatro anos) mas no caso do número ser número com o final 0 mas não for bissexto o programa irá mostrar que é
if ano_bissexto == 0:
    print('\033[32m{} é um ano bissexto\033[m!'.format(ano))
else:
    print('\033[31m{} não é um ano bissexto\033[m!'.format(ano))