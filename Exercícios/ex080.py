'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()). No final, mostre a lista ordenada na tela.'''

numeros = list()

for c in range(0, 5):
    numero = int(input('Digite um número:'))
    if c == 0 or numero > numeros[-1]:
        numeros.append(numero)
    else:
        pos = 0
        while pos < len(numeros):
            if numero <= numeros[pos]:
                numeros.insert(pos, numero)
                break
            pos += 1
print(numeros)