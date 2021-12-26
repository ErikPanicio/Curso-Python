'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

resposta = 'S'
numero = 0
numeros = list()

while resposta == 'S':
    numero = int(input('Digite um número:'))
    resposta = str(input('Quer continuar? [S/N]:').upper())
    if numero in numeros[:]:
        numeros = numeros
    else:
        numeros.append(numero)
numeros.sort()
print(numeros)
