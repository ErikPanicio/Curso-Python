#Crie um programa que faça o computador jogar jokenpô com você

#Programa Complexo

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('[0]Pedra\n[1]Papel\n[2]Tesoura\nDigite o número da jogada:'))
print('-=' * 14)
print('O Jogador Escolheu: {}'.format(itens[jogador]))
print('O Computador Escolheu: {}'.format(itens[computador]))
print('-=' * 14)
if computador == 0:    #Computador Pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('jogador VENCEU!')
    elif jogador == 2:
        print('Computador VENCEU!')
elif computador == 1:   #Computador Papel
    if jogador == 0:
        print('Computador VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Jogador VENCEU!')
elif computador == 2:   #Computador Tesoura
    if jogador == 0:
        print('Jogador VENCEU!')
    elif jogador == 1:
        print('Computador VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
