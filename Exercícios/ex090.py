'''Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura
na tela'''

aluno = {}
aluno['nome'] = str(input("Digite o nome do aluno:"))
aluno['media'] = int(input("Digite a média do aluno:"))
print(f'Nome é igual a {aluno["nome"]}\nMédia é igual a {aluno["media"]}')
if aluno['media'] < 60:
    print('Recuperação')
else:
    print('Aprovado!')
