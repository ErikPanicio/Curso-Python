'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado
e as suas respecivas posições na lista.'''

numeros = list()
maior = 0
menor = 0
ordemMa = 0
ordemMe = 0

for c in range(0, 5):
    numeros.append(int(input(f'Digite o número na posição {c} :')))
    if c == 0:
        maior = numeros[c]
        menor = numeros[c]
    if numeros[c] > maior:
        maior = numeros[c]
        ordemMa = c
    if numeros[c] < menor:
        menor = numeros[c]
        ordemMe = c
print(f'O maior número foi {maior} na posição {ordemMa}\nO menor número foi {menor} na posição {ordemMe}')

