'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final mostre quantos números foram digitados e qual foi a soma  entre eles (desconsiderando o flag)'''

cont = 0
total = 0

while True:
    num = int(input('Digite um número (999 para parar):'))
    if num == 999:
        break
    total = total + num
    cont = cont + 1
print(f'Foram {cont} número(s) digitado(s) e a soma dele(s) foi:{total}')
