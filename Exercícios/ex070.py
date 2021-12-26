'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
Qual foi o total gasto na compra; Quantos produtos custam mais de R$1000; Qual é o nome do produto mais barato'''

cont = 0
soma = 0
menorpreco = 0
produtomenor = ''

while True:
    produto = str(input('Digite o nome do produto:'))
    preco = int(input('Digite o preço do produto:R$'))
    continuar = str(input('Deseja continuar?[S/N]:')).upper()
    soma = soma + preco
    if preco < menorpreco or produtomenor == ' ':     #O valor de menorpreco é 0 (zero não vai ser maior que o valor de produto), então caso seja a primeira repetição o valor de preco irá para menorpreco, pois é a primeira repetição e o cont estará valendo 0.
        menorpreco = preco
        produtomenor = produto
    if preco > 1000:
        cont = cont + 1
    if continuar == 'N':
        print(f'O total gasto na compra foi de:R${soma}\n{cont} produtos custa(m) mais de R$1000\nO nome do produto mais barato é:{produtomenor}')
        break
