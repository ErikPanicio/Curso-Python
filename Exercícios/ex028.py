'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador (programa deverá escrever na tela se o usuário venceu ou perdeu)'''

from random import shuffle

print('Adivinhe o número que eu pensei, entre 0 e 5')
usuario = int(input('Digite o número que o computador pensou:'))
lista = [0, 1, 2, 3, 4, 5]
shuffle(lista)              #Embaralha a lista
computador = lista[0]       #Escolhe o item 0 da lista embaralhada
if usuario == computador:
    print('\033[1;32mVocê acertou PARABÉNS!!!')
else:
    print('\033[1;31mVocê errou!')
print(computador)           #Ver a resposta
