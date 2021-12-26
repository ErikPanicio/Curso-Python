'''Faça um programa que leia a peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos'''

maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input('Digite o {}° peso:'.format(c)))
    if c == 1:               #Se for a primeira repetição só terá um número lido, então por ser o unico esse número será o maior e o menor. Ex: Se tenho 10 e mais nada ele é o maior e o menor número ao mesmo tempo.
        maior = peso
        menor = peso
    else:                    #Se for a segunda repetição ou etc, terá mais de um número.
        if peso > maior:     #Então ele comparará se o peso atual é maior que o peso da váriavel maior, se sim, a váriavel maior receberá o peso atual.Ex: maior = 10 se o novo número é 11 ele substituirá o número da váriavel maior (o mesmo acontece com a váriavel menor).
            maior = peso
        elif peso < menor:   #Ele comparará o novo peso com o peso da váriavel menor, se o peso atual for menor, ele definirá esse peso menor na váriavel menor.
            menor = peso
print('O maior peso foi de {:.1f}Kg'.format(maior))
print('O menor peso foi de {:.1f}kg'.format(menor))
