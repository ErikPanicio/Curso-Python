'''Crie um programa que leia o nome completo de uma pessoa e mostre:
* O nome com todas as letras maiúsculas
* O nome com todas as lestras minúsculas
* Quantas letras ao todo (sem considerar espaços)
* Quantas letras tem o primeiro nome'''

nomecompleto = str(input('Digite seu nome completo:')).strip()
print('O nome em maiúsculo é:{}'.format(nomecompleto.upper()))
print('O nome em minúsculo é:{}'.format(nomecompleto.lower()))
print('O nome têm ao todo:{} letras'.format(len(nomecompleto) - nomecompleto.count(' ')))
nome = nomecompleto.split()
#Defini nome = nomecompleto.split() para que o nome e o sobrenome fiquem em listas diferentes
#Dentro da variavel nome temos duas listas [0] [1]
print('Seu nome é:{} e têm:{} letras'.format(nome[0], len(nome[0])))
#                                                ^      ^ mandei contar quantos caracteres tem na lista [0]
#                                                ^ mandei escrever o que estava na lista [0] (a primeira)