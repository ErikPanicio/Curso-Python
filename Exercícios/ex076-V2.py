'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência. No final, mostre uma listagem de
preços organizando os dados de forma tabular'''

nomepreco = ('Lápis', '1.70', 'Borracha', '2.00', 'Caderno', '15,90', 'Estojo', '25.00', 'Transferidor', '4.20', 'Mochila', '120.00',
             'Canetas', '22.30', 'Livro', '34.90')

for c in range(0, len(nomepreco), 2):
    print(f'{nomepreco[c]:.<30}R${nomepreco[c + 1]}')