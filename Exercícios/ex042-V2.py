'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero:Todos os lados iguais; Isósceles:Dois lados iguais; Escaleno:Todos os lados diferentes'''

reta1 = float(input('Digite a primeira reta:'))
reta2 = float(input('Digite a segunda reta:'))
reta3 = float(input('Digite a terceira reta:'))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Esses segmentos podem formar um triângulo!')
    if reta1 == reta2 == reta3:
        print('Esse triângulo será Equilátero')
    elif reta1 != reta2 != reta3 != reta1:          #Repeti a reta1 de novo para compara-lá com a reta3, se não fizesse isso a reta1 seria diferente da reta2 que seria diferente da reta3 mas a reta3 não seria diferente da reta1.
        print('Esse triângulo será Escaleno')
    else:                                           #Simplificado (preferiria que fosse mais especificado para que diminuísse a chance de dar algum erro, mas é uma maneira de simplificar o código)
        print('Esse triângulo será Isósceles')
else:
    print('Os segmentos não podem formar um triângulo!')
