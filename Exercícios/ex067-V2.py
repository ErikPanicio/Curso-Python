'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo'''

while True:
    num = int(input('Digite um número:'))
    if num < 0:
        break
    for c in range(0, 11):   #Jeito mais correto
        total = num * c
        print(f'{num} x {c} = {total}') #Ou {num} x {c} = {num * c} tirando a váriavel total
print('Fim do Programa!')