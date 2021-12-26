'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo desconsiderando os espaços.
Palíndromo (Frases que podem ser lidas de frente para trás Ex:APOS A SOPA)'''

#Não consegui fazer utilizando a estrutura FOR, deste jeito é muito mais simples.

frase = str(input('Digite uma frase:')).strip().lower()
tras = frase[::-1]
if frase == tras:
    print('Essa frase é um Palíndromo!')
elif frase != tras:
    print('Essa frase não é um Palíndromo!')