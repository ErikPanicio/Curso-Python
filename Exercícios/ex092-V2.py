'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário, se por acaso a carteira
de trabalho for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade,
com quantos anos a pessoa vai se aposentar'''

from datetime import datetime

ano = datetime.today().year

cadastro = {'nome': str(input("Nome:")),
            'idade': ano - (int(input("Ano de nascimento:"))),
            'carteira_trabalho': int(input("Número carteira de trabalho [0 não tem]:"))
            }
if cadastro['carteira_trabalho'] != 0:
    cadastro['ano_contratacao'] = int(input("Ano de contratação:"))     #Se eu fizer isso -> cadastro = {'ano_contratacao': str(input("Ano de contratação"))}, é como se eu tivesse acabado de criar esse dicionário, ele terá apenas o valor de ano_contratacao
    cadastro['salario'] = float(input("Salário: R$"))
    cadastro['aposentadoria'] = ((cadastro['idade'])) - (ano - (cadastro['ano_contratacao'])) + 35  #Vou pegar a idade da pessoa e diminuir o tempo que ela já contribuiu, encontrando assim quando ela começou a trabalhar e soma a esse valor 35 anos e assim descobrir com quantos anos ela vai se aposentar
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')