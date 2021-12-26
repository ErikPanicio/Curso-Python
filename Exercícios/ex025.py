#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' ao nome

nome = str(input('Digite seu nome completo:')).title()
print('Seu nome tem Silva?:{}'.format('Silva' in nome))
#o mesmo problema do anterior