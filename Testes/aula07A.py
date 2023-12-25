n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2 #Adição
m = n1 * n2 #Subtração
d = n1 / n2 #Divisão
di = n1 // n2 #Divisão inteira
e = n1 ** n2 #Exponenciação
print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d ), end=' >>> ') #end faz com que não aja quebra de linha, se digitarmos algo dentro dos parenteses do end ele escreverá está coisa antes da proxima linha
print('Divisão inteira {} e potência {}'.format(di, e))
