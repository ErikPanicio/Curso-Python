'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final coloque
esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado'''

from random import randint
from operator import itemgetter

valores = {}
valores['jogador1'] = randint(0, 6)
valores['jogador2'] = randint(0, 6)
valores['jogador3'] = randint(0, 6)
valores['jogador4'] = randint(0, 6)
organizacao = {}
organizacao = sorted(valores.items(), key=itemgetter(1), reverse=True)    #Minha chave vai ser o radint, ele vai organizar pelo número aleatório, se fosse itemgetter(0) ele iria organizar pelo jogador, do 1 ao 4. Reverse = True para mostrar o maior valor e não o menor
for i, j in enumerate(organizacao):
    print(f'{i + 1}° Lugar: {j[0]} valor:{j[1]}')

#Não entendi 100%