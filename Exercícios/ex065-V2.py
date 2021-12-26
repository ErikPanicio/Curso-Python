'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar os valores'''

continuar = 1
cont = 0
maior = 0
menor = 0
total = 0

while continuar == 1:
    num = int(input('Digite um número:'))
    cont = cont + 1
    total = total + num
    if cont == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    continuar = int(input('Você deseja continuar? \n[1]Sim \n[2]Não \nDigite sua resposta:'))
media = total / cont
print('A média dos números digitados foi de {:.2f}, o maior número digitado foi {}, e o menor número digitado foi {}.'.format(media, maior, menor))