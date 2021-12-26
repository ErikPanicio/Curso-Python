#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-lá,sabendo que cada litro de tinta,pinta uma área de 2m²

largura = float(input('Digite a largura da parede:'))
altura = float(input('Digite a altura da parede:'))
area = largura*altura
print('A área da sua parede é de:{:.2f}m² \nPara pintar sua parede é preciso de:{} litros de tinta'.format(area, area/2))
