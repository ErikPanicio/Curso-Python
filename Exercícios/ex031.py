'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,cobrando R$0,50
por Km para viagens de até 200Km e R$0,45 para viagens mais longas'''

distancia = float(input('Digite a distância da sua viagem:'))
if distancia <= 200:
    print('Você irá pagar \033[1;32mR${:.2f}\033[m, pela viagem de \033[1;30m{} Km\033[m '.format(distancia * 0.50, distancia))
else:
    print('Você irá pagar \033[1;32mR${:.2f}\033[m, pela viagem de \033[1;30m{} Km\033[m'.format(distancia * 0.45, distancia))
