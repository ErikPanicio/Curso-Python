'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
encontra no intervalo de 1 até 500'''

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:             #Identifica se é Par ou Ímpar e se é multiplo de 3
        cont = cont + 1        #Quantos números foram aceitos pelo if
        soma = soma + c        #Soma de todos os número ímpares multiplos de 3
print('O resultado dos {} números somados foi de:{}'.format(cont, soma))
