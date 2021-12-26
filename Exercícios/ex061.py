'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de um PA, mostrando os 10 primeiros termos da progressão,
usando a estrutura while.'''

termo = int(input('Digite o Termo:'))
razao = int(input('Digite a Razão da PA:'))
iniciofim = 0

while iniciofim != 10:
    print(termo, end=' ')
    termo = termo + razao       #Vai somar o termo com a razão e o resultado irá somar com a razão novamente
    iniciofim = iniciofim + 1   #Quando o contador chegar em 10 essa repetição acaba
