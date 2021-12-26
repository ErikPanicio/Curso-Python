'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou, no final do jogo'''

from random import randint

cont = 0

while True:
    num = int(input('Digite um número:'))
    escolha = str(input('Você quer Par ou Ímpar [P/I]:')).upper()
    num2 = randint(0, 10)
    soma = num + num2
    if escolha == 'P' or escolha == 'I':
        print(f'O usuário digitou {num} e o computador {num2} o total é {soma}')
        if escolha == 'P':
            if soma % 2 == 0:
                print('Jogador Venceu!')
                cont = cont + 1
            else:
                print('Computador Venceu!')
                break
        if escolha == 'I':
            if soma % 2 == 1:
                print('Jogador Venceu')
                cont = cont + 1
            else:
                print('Computador Venceu!')
                break
    else:
        print('ERRO')
print(f'Você venceu {cont} vez(es)!')