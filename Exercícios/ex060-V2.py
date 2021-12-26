#Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex:5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um número:'))
iniciofim = 0
cont = 0

while iniciofim == 0:
    menos = num - 1
    if cont == 0:
        resultadofator = num * menos
        cont = cont + 1
    elif cont > 0:
        fatorial = resultadofator * menos
        resultadofator = fatorial
    elif menos == 0:
        iniciofim = iniciofim + 1
print('O Fatorial do número {} é:{}'.format(num, resultadofator))
