'''Faça um programa que leia 5 valores numéripos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado
e as suas respepivas posições na lista.'''

numeros = list()
maior = 0
menor = 0
posicaoMa = 0
posicaoMe = 0

for p in range(0, 5):
    numeros.append(int(input(f'Digite o número na posição {p}:')))
    if p == 0:
        maior = numeros[p]
        menor = numeros[p]
    if numeros[p] > maior:
        maior = numeros[p]
        posicaoMa = p
    if numeros[p] < menor:
        menor = numeros[p]
        posicaoMe = p

print(f'O maior número foi {maior} na posição {posicaoMa}', end=' ')

for p in range(0, 5):
    if numeros[p] == maior and p != posicaoMa:      #Se o número p da lista for igual ao maior número, significa que este também é o maior número; se esse o maior número está na posição 1 e o maior número está na posição 1, então o maior número é o mesmo, logo não preciso printá-lo, porque já printei, então, se o maior valor for encontrado em outra posição tenho que printá-lo, porque este é outro maior valor
        print(f'e na posição {p}', end=' ')         #Resumindo: 10 maior número, na posição 1 (printado lá em cima); caso o programa encontre o valor 10 na posição 1 ele não vai printar, porque é o mesmo valor; mas se ele encontrar o maior valor em outra posição, este é outro maior valor, logo devo printá-lo

print(f'\nO menor número foi {menor} na posição {posicaoMe}', end=' ')

for p in range (0, 5):
    if numeros[p] == menor and p != posicaoMe:
        print(f'e na posição {p} ')
