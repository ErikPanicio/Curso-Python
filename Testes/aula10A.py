n1 = float(input('Digite sua nota 1: '))
n2 = float(input('Digite sua nota 2: '))
media = (n1 + n2)/2
print('Sua média foi de:{}'.format(media))
if media >= 6.0:
    print('Sua média foi boa, PARABÉNS')
else:
    print('Sua média está ruim, ESTUDE MAIS')