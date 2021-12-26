#Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex:5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um número:'))
menos = num - 1                     #Ex: 5 - 1 = 4
fatorial = num * menos              #Ex: 5 * 4 = 20 (esse 4 vem da variável menos)

while menos != 1:
    menos = menos - 1               #Ex: 4 - 1 = 3 (primeiro loop), 3 - 1 = 2 (segundo loop)...
    fatorial = fatorial * menos     #Ex: fatorial = 20 * 4 = 80 (primeiro loop), fatorial = 80 * 3 = 240 (segundo loop)...
print('O fatorial de {} é: {}'.format(num, fatorial))
