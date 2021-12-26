#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

ano = int(input('Digite o ano:'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:       #Ano bissexto ocorrerá a cada quatro anos (exceto anos múltiplos de 100 que não são múltiplos de 400).Então Dividirá o ano por quatro para achar o valor 0 que vai aparecer de quatro em quatro números (0, 1, 2, 3, 0...). Dividirá por 100 porque: não é bissexto números múltiplos de 100, por isso será diferente de 0 ( != 0 ). Mas ano bissexto pode ser múltiplo de 400 então dividirá por 400 e se for igual a 0 será bissexto
    print('\033[32m{} é um ano bissexto\033[m!'.format(ano))
else:
    print('\033[31m{} não é um ano bissexto\033[m'.format(ano))
