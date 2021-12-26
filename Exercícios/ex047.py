#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

for c in range(1, 51):
    if c % 2 == 0:        #c % 2 = Se o número for divisivel por 2
        print(c, end=' ') #end=' ' para deixar os número na horizontal
