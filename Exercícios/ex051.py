'''Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética. No final, mostre os 10 primeiros
termos dessa progressão'''

termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
decimo = termo + (11 - 1) * razao       #Para conseguir repetir dez vezes os N°s independentemente do termo
for c in range(termo, decimo, razao):   #(N° Que começa a sequência, às dez repetições, quantos em quantos N°s vão pulando)
    print(c, end=' ')
