'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador (programa deverá escrever na tela se o usuário venceu ou perdeu)'''

from random import randint

print('Adivinhe o número que eu pensei, entre 0 e 5')
usuario = int(input('\nDigite o número que o computador pensou:'))
computador = randint(0, 5)      #Escolhe um número aleatório entre 0 e 5
if usuario == computador:
    print('\033[1;32mVocê acertou PARABÉNS!!!')
else:
    print('\033[1;31mVocê errou!')
print(computador)               #Ver a resposta