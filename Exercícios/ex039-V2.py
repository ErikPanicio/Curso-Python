'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
Se ele ainda vai se alistar ao serviço militar; Se é a hora de se alistar; Se ja passou do tempo de alistamento; Seu programa também
deverá mostrar o tempo que falta ou que passou do prazo'''

from datetime import date

ano_nascimento = int(input('Digite seu ano de nascimento:'))
idade = date.today().year - ano_nascimento
if idade == 18:
    print('É hora de se alistar ao exército!')
elif idade > 18:
    idade_passou = idade - 18
    ano = date.today().year - idade_passou
    print('Já passou {} ano(s) do tempo de se alistar!\nSeu alistamento foi em {}'.format(idade_passou, ano))
elif idade < 18:
    idade_falta = 18 - idade
    ano = date.today().year + idade_falta
    print('Ainda falta {} ano(s) para se alistar!\nSeu alistamento será em {}'.format(idade_falta, ano))