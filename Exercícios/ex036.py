'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal,sabendo que ela não pode exceder
30% salário ou então o empréstimo será negado.'''

casa = float(input('Digite o valor da casa:R$'))
salario = float(input('Digite o valor do seu salário:R$'))
anos = int(input('Digite em quantos anos pretende pagar a casa:'))
prestacao_mensal = casa / (anos * 12)
salario_30 = (salario / 100) * 30
if prestacao_mensal <= salario_30:
    print('\033[32mSeu empréstimo foi aceito\033[m')
    print('O valor mensal será:R${:.2f}, para serem pagos em {} anos'.format(prestacao_mensal, anos))
elif prestacao_mensal > salario_30:
    print('\033[31mSeu empréstimo foi negado')