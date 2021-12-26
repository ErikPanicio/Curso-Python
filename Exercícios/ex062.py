'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.'''

termo = int(input('Digite o Termo:'))
razao = int(input('Digite a Razão da PA:'))
iniciofim = 0
continuar = 1
termos = 9

while continuar != 0:
    termos = termos + continuar     #(Se o usuário quiser continuar) Irá somar os 10 termos (termos = 9 por que já soma + 1 com o continuar então será termos = 10) com o valor que o usuário digitar, para que a repetição de baixo repita as vezes que o usuário digitou, já que o programa já repetiu 10 vezes no inicio, irá somar com esses 10 e o valor somado será repetido, tirando os 10 já repetidos
    while iniciofim != termos:      #A primeira repetição o valor de termos será 10, depois será somado esse 10 com o valor que o usuário digitar. Ex: termos = 10 + continuar = 5, termos = 15 já repetiu 10 vezes no incio então repetirá mais 5, que são as vezes que o usuário digitou
        print(termo, end=' ')
        termo = termo + razao       #Vai somar o termo com a razão e o resultado irá somar com a razão novamente
        iniciofim = iniciofim + 1   #Quando o contador chegar em termos que vale 10 essa repetição acaba
    continuar = int(input('\nQuantos termos você quer mostrar a mais?:')) #Irá perguntar para o usuário se quer continuar e o valor adicionado será somado à variável termos
print('Foram mostrados {} termos no total'.format(iniciofim))