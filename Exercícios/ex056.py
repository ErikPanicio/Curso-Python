'''Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa,
mostre: A média de idade do grupo; Qual é o nome do homem mais velho; Quantas mulheres têm menos de 20 anos.'''

somaidade = 0
maioridadehomem = 0
nomemaisvelhohomem = ''
menosdevinte = 0

for c in range(1, 5):
    nome = str(input('--- {}ª Pessoa ---\nNome:'.format(c)))
    idade = int(input('Idade:'))
    genero = str(input('Gênero [M/F]:').upper())
    somaidade = somaidade + idade
    media = somaidade / 4                               #Média das idades
    if genero == 'M':
        M = 'Masculino'
    elif genero == 'F':
        F = 'Feminino'
    if c == 1 and genero == 'M':
        maioridadehomem = maioridadehomem + idade       #Idade e nome do primeiro homem mais velho, já que ele é o primeiro independentemente da idade ele será o mais velho
        nomemaisvelhohomem = nome
    elif c > 1 and genero == 'M':
        maioridadehomem = idade                         #Homem mais velho
        nomemaisvelhohomem = nome
    if idade < 20 and genero == 'F':
        menosdevinte = menosdevinte + 1                 #Quantas mulheres com menos de vinte anos
print('''A média de idade do grupo é de:{} anos\nO nome do homem mais velho é:{} e a idade dele é de:{} anos
{} mulher(es) tem menos de vinte anos!'''.format(media, nomemaisvelhohomem, maioridadehomem, menosdevinte))
