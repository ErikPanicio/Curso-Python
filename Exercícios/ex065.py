'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar os valores'''

iniciofim = 0
soma = 0
cont = 0
maior = 0
menor = 0

while iniciofim == 0:
    num = int(input('\033[34mDigite um número:\033[m'))
    soma = soma + num       #A soma dos valores digitados
    cont = cont + 1         #Quantos valores foram digitados
    continuar = int(input('Você deseja continuar a digitar números?\n\033[32m[1]Sim\n[2]Não\033[m\nDigite sua resposta:'))
    if num > maior:
        maior = num
        if menor == 0:      #Por menor valer 0, na primeira repetição a variável menor irá receber o primeiro número digitado, para que, caso todos os números digitados sejam iguais o menor e o maior número também serão iguais
            menor = num
    elif num < maior:
        menor = num
    if continuar == 2:
        iniciofim = iniciofim + 1
        media = soma / cont
        print('A média dos números digitados foi de {:.2f}, o maior número digitado foi {}, e o menor número digitado foi {}'.format(media, maior, menor))
