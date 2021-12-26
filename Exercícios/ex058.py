'''Melhore o jogo do DESAFIO 028 onde o computador "pensa" em um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import shuffle

usuario = int(input('Adivinhe o número que eu pensei, entre 0 e 10!\nDigite o número que o computador pensou:'))
cont = 0
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(lista)
computador = lista[0]

while usuario != computador:
    usuario = int(input('\033[31mVocê errou!!!\033[m\nDigite novamente o número que o computador pensou:'))
    cont = cont + 1
if usuario == computador:
    cont = cont + 1
    print('\033[32mParabéns você acertou!!!\033[m\nVocê tentou {} vezes até acertar!'.format(cont))
