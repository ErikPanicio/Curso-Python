#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente; Ex:Ana Maria de Souza; primeiro = Ana; Último = Souza

nomecompleto = str(input('Digite seu nome completo:')).strip().split()
print('\033[34mSeu primeiro nome é:\033[m\033[1m {} \033[m\n\033[34mSeu último nome é:\033[m\033[1m {} \033[m'.format(nomecompleto[0], nomecompleto[-1]))