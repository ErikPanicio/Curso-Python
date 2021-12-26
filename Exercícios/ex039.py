'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
Se ele ainda vai se alistar ao serviço militar; Se é a hora de se alistar; Se ja passou do tempo de alistamento; Seu programa também
deverá mostrar o tempo que falta ou que passou do prazo'''

ano_nascimento = int(input('Digite seu ano de nascimento:'))
idade = 2020 - ano_nascimento
if idade == 18:
    print('É hora de se alistar ao exército!')
elif idade > 18:
    idade_passou = idade - 18
    print('Já passou {} ano(s) do tempo de se alistar!'.format(idade_passou))
elif idade < 18:
    idade_falta = 18 - idade
    print('Ainda falta {} ano(s) para se alistar!'.format(idade_falta))