'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo'''


cont = 0

while True:         #Utilizando o While True
    if cont == 0 or cont == 10:
        num = int(input('Digite um número para mostrar sua tabuada:'))
        if cont == 10:
            cont = 0
    if num < 0:
        print('Fim do Programa!')
        break
    cont = cont + 1
    total = num * cont
    print(f'{num} x {cont} = {total}')
