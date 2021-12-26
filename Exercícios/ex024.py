#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'

cidade = str(input('Digite o nome de uma cidade:')).strip().capitalize().split()
print('Santos' in cidade[0])
#esse código tem um erro pois se for escrito por Ex: Santosss o programa ainda da TRUE