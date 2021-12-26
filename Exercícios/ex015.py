#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar,sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

km = float(input('Digite a quantidade de Km(s) percorridos:'))
dias = int(input('Digite quantos dias esse carro foi alugado:'))
valor = (km * 0.15) + (dias * 60)
print('o valor a ser pago é:R${:.2f}'.format(valor))