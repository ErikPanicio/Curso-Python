'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados;
B)A lista de valores, ordenada de forma decrescente; C)Se o valor 5 foi digitado e está ou não na lista.'''


numeros = list()
cont = 0

while True:
    numeros.append(int(input('Digite um número:')))
    continuar = str(input('Deseja Continuar? [S/N]:').upper())
    cont = cont + 1
    numeros.sort(reverse=True)
    if continuar == 'N':
        break
    if 5 in numeros:
        cinco = 'O número cinco está na lista!'
    else:
        cinco = 'O número cinco não está na lista!'
print(f'Foram digitados {cont} números\nOs números são: {numeros}\n{cinco}')