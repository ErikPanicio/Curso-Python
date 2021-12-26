'''A Conferedeção Nacional precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
Até 9 anos:MIRIM; Até 14 anos:INFANTIL; Até 19 anos:JUNIOR; Até 20 anos:SÊNIOR; Acima:MASTER'''

from datetime import date

ano = int(input('Digite seu ano de nascimento:'))
idade = date.today().year - ano

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')          #Maneira simplificada
elif idade <= 20:
    print('Sênior')
else:
    print('Master')
