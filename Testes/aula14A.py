#Irá mostrar todos os números que forem menores do que 10.
'''
c = 1

while c < 10:
    print(c)
    c = c + 1
'''

#Enquanto o número digitado for diferente de 0 o programa irá pedir números infinitamente.
'''
n = 1

while n != 0:
    n = int(input('Digite um número:'))
print('Fim')
'''

#O programa irá pedir números e te perguntar se quer continuar digitando números, enquanto você digitar 'S' ele irá pedir mais números, digitando 'N' ele irá parar de pedir.
'''
r = 'S'

while r == 'S':
    n = int(input('Digite um número:'))
    r = str(input('Você quer continuar? [S/N]:')).upper()
print('Fim')
'''

#Enquanto o número digitado for diferente de 0 o programa irá pedir números e quando você digitar 0 ele irá parar de pedir número e irá mostrar quantos números pares e quantos ímpares foram digitados.
'''
n = 1
par = 0
impar = 0

while n != 0:
    n = int(input('Digite um número:'))
    if n != 0:                  #Para o 0 não ser contado como par
        if n % 2 == 0:          #Se o número dividido por 2 tiver o resto da divisão igual a 0
            par = par + 1
        else:
            impar = impar + 1
print('Entre os números digitados tiveram {} número pares e {} número ímpares'.format(par, impar))
'''