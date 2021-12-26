#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

#Maneira mais rápida, ao invés de fazer duas vezes o trabalho (pegar os pares e pegar os ímpares e não mostra os ímpares), ele apenas pega os pares. (Uma maneira que gasta menos memória e etc)

for c in range(2, 51, 2):
    print(c, end=' ') #end=' ' para deixar os número na horizontal
