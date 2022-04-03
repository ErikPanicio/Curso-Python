'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear
6 números entre 1 e 60 para cada jogo, cadastando tudo em uma lista composta (os números não podem se repetir)'''

from random import randint

lista = []
jogos = int(input("Quantos jogos serão jogados?:"))

for c in range(0, jogos):
    for i in range(0, 6):
        aleatorio = randint(1, 60)
        if aleatorio not in lista:
            lista.append(aleatorio)
        elif aleatorio in lista:        #Se tivesse um "if" aqui ele rodaria os dois "ifs" ao mesmo tempo e daria muitos valores além de 6
            while aleatorio in lista:
                aleatorio = randint(1, 60)
            lista.append(aleatorio)
    print(f"Os números são:{lista}")
    lista.clear()

#Sempre terá 6 valores e nunca se repetirão na mesma lista

'''
    #Código de teste (colocar antes do lista.clear)
    
    print(f"{len(lista)}")
    if lista.count(6) == 2:
        print("\033[1;31m ERRO\033[m")
'''