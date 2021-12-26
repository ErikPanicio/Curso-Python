'''Escreva um programa que leia a velocidade de um carro (se ele ultrapassar 80Km/h),
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite)'''

velocidade = float(input('Digite a velocidade do carro Km:'))
if velocidade > 80:
    velocidade_acima = velocidade - 80
    print('\033[31mVocê está acima da velocidade permitida!')
    print('Sua multa é de:\033[1mR${:.2f}\033[m'.format(velocidade_acima * 7))
else:
    print('\033[1;32mVocê está na velocidade permitida!')


'''Poderia não utilizar o ELSE, colocando o print() encostado na borda para sempre ser executado,
então sempre que a velocidade fosse menor ou igual a 80 iria mostrar a mensagem do print() que esta agora dentro do ELSE'''
