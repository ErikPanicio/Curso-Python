#Crie um programa que faça o computador jogar jokenpô com você

#Programa Simples

from random import randint

usuario = int(input('[1]Pedra\n[2]Papel\n[3]Tesoura\nDigite o número da jogada:'))
computador = randint(1, 3)
if usuario == computador:
    print('Empate')
elif usuario == 1 and computador == 2:
    print('Você perdeu!')
elif usuario == 1 and computador == 3:
    print('Você venceu!')
elif usuario == 2 and computador == 1:
    print('Você venceu!')
elif usuario == 2 and computador == 3:
    print('Você perdeu!')
elif usuario == 3 and computador == 1:
    print('Você perdeu!')
elif usuario == 3 and computador == 2:
    print('Você venceu!')
else:
    print('Esse número não está incluso')
print(computador)
