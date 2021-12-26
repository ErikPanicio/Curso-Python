'''Crie um programa que leia dois valores e mostre um menu na tela: [1]Somar, [2]Multiplicar, [3]Maior, [4]Novos números,
[5]Sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.'''

num1 = int(input('Digite o primeiro valor:'))
num2 = int(input('Digite o segundo valor:'))
escolha = 0

while escolha != 5:
    escolha = int(input('\033[30mSelecione sua escolha:\033[m \n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos Números\n[5]Sair do Programa\n\033[1;34mDigite sua escolha:\033[m'))
    if escolha == 1:                            #SOMA
        print('A soma de {} + {} é igual a {}'.format(num1, num2, num1 + num2))
    elif escolha == 2:                          #MULTIPLICAÇÃO
        print('A multiplicação de {} * {} é igual a {}'.format(num1, num2, num1 * num2))
    elif escolha == 3 and num1 > num2:          #MAIOR NÚMERO 1
        print('Entre os números {} e {} o maior é {}'.format(num1, num2, num1))
    elif escolha == 3 and num2 > num1:          #MAIOR NÚMERO 2
        print('Entre os número {} e {} o maior e {}'.format(num1, num2, num2))
    elif escolha == 3 and num1 == num2:         #SE OS NÚMERO FOREM IGUAIS
        print('Os número são iguais!')
    elif escolha == 4:                          #PEDIR NOVAMENTE OS NÚMEROS
        num1 = int(input('Digite novamente o primeiro valor:'))
        num2 = int(input('Digite novamento o segundo valor:'))
    elif escolha == 5:                          #FINALIZAR PROGRAMA
        print('\033[30mPrograma Finalizado!')
    else:
        print('\033[31mOpção Inválida! Tente novamente!')
