'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em um tupla. No final mostre: A)Quantas vezes apareceu o valor 9;
B)Em que posição foi digitado o primeiro valor 3;C)Quais foram os números pares'''

numeros = (int(input('Digite um número:')), int(input('Digite um número:')), int(input('Digite um número:')), int(input('Digite um número:')))

print(f'O número nove apareceu: {numeros.count(9)} vez(es)')        #Quantas vezes apareceu o nove

if 3 in numeros:                                                    #Em qual posição apareceu o 3
    print(f'O número três aparece na posição: {numeros.index(3)+1}')
else:
    print('O número três não foi digitado!')

print('Os números pares são:', end=' ')
for c in range(0,4):                                                #Números pares
    if numeros[c] % 2 == 0:
        print(numeros[c], end= ' ')
