'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()). No final, mostre a lista ordenada na tela.'''

numeros = list()
cont = 0

for c in range(0, 5):
    numero = (int(input('Digite um número:')))
    print(c)
    if c == 0:
        numeros.append(numero)
        cont = cont + 1
    if c == 1:
        numeros.append(numero)
        cont = cont + 1
    elif c == 1 and numeros[c] < numeros[0]:
        numeros.insert(0, numero)
        cont = cont + 1

for c in range(0, 5):
    for v in range(0, 5):       # Não têm mais de 1 ou 2 elementos, então dará erro, já que ele comparará o valor com outro que nem foi digitado ainda
        if numeros[c] > numeros[v]:
            numeros.insert(v, numeros[c])
        if numeros[c] < numeros[v]:
            numeros.insert(v, numeros[c - 1])
print(numeros[:])






'''        
    if cont == 1 and numeros[c] > numeros[0]:
        numeros.append(numero)
        cont = cont + 1
    if cont == 1 and numeros[c] < numeros[0]:
        numeros.insert(0, numero)
        cont = cont + 1

    if numeros[c] > numeros[0]:
        numeros.append(int(input('Digite um número:')))
'''
