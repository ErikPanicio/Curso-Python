'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
À vista dinheiro/cheque:10% de desconto; À vista no cartão:5% de desconto; Em até 2x no cartão:Preço normal; 3x ou mais no cartão:20% de juros'''

valor_produto = float(input('Digite o valor o produto:'))
forma_pagamento = int(input('[1] À vista Dinheiro/Cheque \n[2] À vista Cartão\n[3] 2x no Cartão\n[4] 3x ou mais no Cartão\nDigite a opção que deseja pagar:'))
if forma_pagamento == 1:
    total = valor_produto - ((valor_produto / 100) * 10)
    print('O valor a ser pago é de:R$ {:.2f}'.format(total))
elif forma_pagamento == 2:
    total = valor_produto - ((valor_produto / 100) * 5)
    print('O valor a ser pago é de:R$ {:.2f}'.format(total))
elif forma_pagamento == 3:
    total = valor_produto
    parcela = valor_produto / 2
    print('O valor total é de:R$ {:.2f} e você pagará em 2x de:R$ {:.2f}'.format(total, parcela))
elif forma_pagamento == 4:
    quantidadeparcela = int(input('Serão em quantas parcelas:'))
    total = valor_produto + ((valor_produto / 100) * 20)
    parcela = total / quantidadeparcela
    print('O valor total é de:R$ {:.2f} com 20% de Juros e você pagará em {}x de: R$ {:.2f}'.format(total, quantidadeparcela, parcela))
else:
    print('\033[31mOpção Errada!')