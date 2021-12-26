'''Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado (número
inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. Considere que o caixa possua cédulas de: R$50, R$20, R$10, R$1'''

cinquenta = 0
vinte = 0
dez = 0
um = 0

valor = int(input('Digite o valor a ser sacado:R$'))

while True:
    if valor >= 50:
        valor = valor - 50
        cinquenta = cinquenta + 1
    else:
        if valor >= 20:
            valor = valor - 20
            vinte = vinte + 1
        else:
            if valor >= 10:
                valor = valor - 10
                dez = dez + 1
            else:
                if valor >= 1:
                    valor = valor - 1
                    um = um + 1
    if valor == 0:
        break
print(f'Foram sacados:\n{cinquenta} Cedula(s) de R$50\n{vinte} Cedula(s) de R$20\n{dez} Cedula(s) de R$10\n{um} Cedula(s) de R$1')