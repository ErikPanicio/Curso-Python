'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os
valores pares e os valores ímpares digitados, respectivamente. Ao final mostre o conteúdo das três listas geradas.'''

numeros = []
pares = []
impares = []

while True:
    numeros.append(int(input('Digite um número:')))
    resposta = str(input('Deseja continuar? [S/N]:').upper())
    if resposta == 'N':
        break
for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        pares.append(numeros[c])
    if numeros[c] % 2 == 1:
        impares.append(numeros[c])

print(f'Números: {numeros}\nPares: {pares}\nÍmpares: {impares}')

