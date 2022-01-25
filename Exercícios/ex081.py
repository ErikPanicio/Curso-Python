'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados;
B)A lista de valores, ordenada de forma decrescente; C)Se o valor 5 foi digitado e está ou não na lista.'''


numeros = list()
cont = 0

while True:
    numeros.append(int(input('Digite um número:')))
    continuar = str(input('Deseja Continuar? [S/N]:').upper())
    if continuar != 'S' and continuar != 'N':
        print('Valor digitado errado!')
        del numeros[-1]
    else:
        cont = cont + 1
        if continuar == 'N':
            break
        if 5 in numeros:
            cinco = 'O número cinco está na lista!'
        else:
            cinco = 'O número cinco não está na lista!'
numeros.sort(reverse=True)
print(f'Foram digitados {cont} números\nOs números são: {numeros}\n{cinco}')