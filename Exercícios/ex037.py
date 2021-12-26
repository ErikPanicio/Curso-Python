'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base da conversão: 1: para Binário; 2: para Octal; 3: para Hexadecimal'''

num = int(input('Digite um número para a conversão:'))
escolha = int(input('Escolha a opção de conversão\n[1]Binário\n[2]Octal\n[3]Hexadecimal\nDigite sua escolha:'))
if escolha == 1:
    print('{} convertido para Binário é {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} convertido para Octal é {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} convertido para Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida')