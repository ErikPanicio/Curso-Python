'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntar se o usuário quer ou não
continuar. No final, mostre: Quantas pessoas tem mais de 18 anos; Quantos homens foram cadastrados; Quantas mulheres tem menos de 20 anos'''

cont_idade = 0
cont_homem = 0
cont_mulher = 0

while True:
    idade = int(input('Digite sua idade:'))
    genero = ' '
    while genero not in 'MF':               #Para que caso o usuário erre na digitação o programa peça novamente o valor
        genero = str(input('Digite seu gênero [M/F]:')).upper()
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar a cadastrar? [S/N]:')).upper()
    if idade > 18:
        cont_idade = cont_idade + 1
    if genero == 'M':
        cont_homem = cont_homem + 1
    if genero == 'F' and idade < 20:
        cont_mulher = cont_mulher + 1
    if resposta == 'N':
        print(f'Há {cont_idade} pessoas com mais de 18 anos \nHá {cont_homem} homens cadastrados \nHá {cont_mulher} mulheres com menos de 20 anos!')
        break
