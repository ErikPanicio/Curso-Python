'''Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra 'A'
*Em que posição ela aparece a primeira vez
*Em que posição ela aparece a última vez'''

frase = str(input('Digite uma frase:')).lower().strip()
print('Aparece \033[1;30m {} \033[m vezes a letra A, ela aparece pela primeira vez na posição:\033[1;30m {} \033[m, e aparece pela última vez na posição:\033[1;30m {} \033[m'.format(frase.count('a'), frase.find('a')+1, frase.rfind('a')+1))
# + 1 adicionado para o usuário entender a posição caso o usuário não saiba que na programação se inicia a contagem em 0