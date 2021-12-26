'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
Abaixo de 18.5:Abaixo do Peso ideal; Entre 18.5 e 25:Peso ideal; 25 até 30:Sobrepeso; 30 até 40:Obesidade; Acima de 40:Obesidade mórbida'''

altura = float(input('Digite sua altura:'))
peso = float(input('Digite o seu peso:'))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu IMC é de:{:.2f}\nVocê está abaixo do peso ideal!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é de:{:.2f}\nVocê está no peso ideal!'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é de:{:.2f}\nVocê está com sobrepeso!'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é de:{:.2f}\nVocê está com obesidade!'.format(imc))
elif imc > 40:
    print('Seu IMC é de:{:.2f}\nVocê está com obsedidade mórbida!'.format(imc))
