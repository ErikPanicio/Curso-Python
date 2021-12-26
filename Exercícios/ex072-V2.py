'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número
pelo teclado (entre 0 e 20) e mostra-lá por extenso'''

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

resposta = ''

while resposta != 'N':
    while True:
        numero = int(input('Digite um número entre 0 e 20:'))
        if numero >= 0 and numero <= 20:
            break
    print(f'O número {numero} por extenso é:{numeros[numero]}')
    resposta = str(input('Quer continuar? [S/N]:')).upper()