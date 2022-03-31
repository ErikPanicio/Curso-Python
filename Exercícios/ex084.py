'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A)Quantas pessoas foram
cadastradas; B)Uma listagem com as pessoas mais pesadas; C)Uma listagem com as pessoas mais leves (só com duas listas)'''

lista = list()
lista_organizada = list()
continuar = 'S'
pessoas = 0
maior = 0
menor = 0
nome_maior = ""
nome_menor = ""

while continuar == 'S':
    lista.append(str(input('Digite seu nome:')))
    lista.append(float(input('Digite seu peso:')))
    lista_organizada.append(lista[:])
    lista.clear()
    pessoas += 1
    continuar = str(input('Deseja continuar? [S/N]:').upper())
    for p in range(pessoas):
        for c in range(pessoas):
            if pessoas == 1:
                maior = lista_organizada[p][1]
                menor = lista_organizada[p][1]
            if lista_organizada[c][1] > maior:
                maior = lista_organizada[p][1]
                nome_maior = lista_organizada[p][0]
            if lista_organizada[c][1] < menor:
                menor = lista_organizada[p][1]
                nome_menor = lista_organizada[p][0]
            if lista_organizada[c][1] == maior:
                nome_maior = nome_maior, lista_organizada[c][0]
for p in lista_organizada:
    if p[1] == maior:
        print(f"Maior = {p[0]}")
print(f"Pessoas cadastradas: {pessoas}\nA(s) pessoa(s) mais pesada(s): {nome_maior}\nA(s) pessoa(s) mais leve(s): {nome_menor}")

#Caso os pesos forem iguais escrever o nome das pessoas pesadas (no momento só escreve de um)