''' Crie um programa que leia o nome completo de uma pessoa e mostre:
* O nome com todas as letras maiúsculas
* O nome com todas as lestras minúsculas
* Quantas letras ao todo (sem considerar espaços)
* Quantas letras tem o primeiro nome '''

nomecompleto = str(input('Digite seu nome completo:')).strip() #.strip para que qualquer espaço dado no inicio ou no final seja negado
print('O nome em maiúsculo é:{}'.format(nomecompleto.upper()))
print('O nome em minúsculo é:{}'.format(nomecompleto.lower()))
print('O nome têm ao todo:{} letras'.format(len(nomecompleto) - nomecompleto.count(' ')))
#.format(len(nomecompleto) - nomecompleto.count(' ')) <----- conte o N° de caracteres na variavel nomecompleto MENOS os números de espaços
print('Seu primeiro nome têm:{} letras'.format(nomecompleto.find(' ')))