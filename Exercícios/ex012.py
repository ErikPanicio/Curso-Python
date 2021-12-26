#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço ,com 5% de desconto

preço = float(input('Digite o preço do produto:R$'))
d = (preço/100)*5
print('o 5% de desconto vale:R${:.2f}, o valor total do produto é:R${:.2f}'.format(d, preço-d))
