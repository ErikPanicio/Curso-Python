'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag - o número 999 da soma)'''

cont = 0
soma = 0
iniciofim = 0

while iniciofim == 0:
    num = int(input('Digite um número (999 para parar o programa):'))
    if num != 999:
        cont = cont + 1
        soma = soma + num
    elif num == 999:
        iniciofim = iniciofim + 1
print('Foram digitado(s) {} número(s) e a soma dele(s) é {}'.format(cont, soma))
