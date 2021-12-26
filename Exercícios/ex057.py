'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
digitalização novamente até ter um valor correto.'''

genero = str(input('Digite seu gênero [M/F]:')).upper()

while genero != 'M' and genero != 'F':  #Or não funciona na estrutura while
    genero = str(input('O valor digitado foi incorreto!\nDigite novamente seu gênero [M/F]:')).upper()
print('Dados aceitos!')