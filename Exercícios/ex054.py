'''Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda
nõa atingiram a maioridade e quantas já são maiores (maioridade 21 anos)'''

from datetime import date

cont = 0
cont2 = 0

for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa:'.format(c)))
    idade = date.today().year - ano
    if idade >= 21:
        cont = cont + 1
    elif idade < 21:
        cont2 = cont2 + 1
print('{} são maiores de idade!'.format(cont))
print('{} não atingiram a maioridade!'.format(cont2))
