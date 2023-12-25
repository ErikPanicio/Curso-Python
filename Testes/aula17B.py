'''valores = list()    #Uma lista pode ser criada assim também
for c in range(0,5):
    valores.append(int(input('Digite um número:')))
print(valores)'''

'''a = [1, 3, 5, 6]
b = a           #Quando se iguala uma lista em Python,  quando uma lista muda a outra muda também (elas se "ligam")
b[0] = 50
print(f'Lista A:{a}\nLista B:{b}')'''

a = [1, 3, 5, 6]
b = a[:]        #A lista b vai receber todos os elementos da lista a, isso significa que a lista b, quando alterada, não mudará os valores da lista a
b[0] = 50
print(f'Lista A:{a}\nLista B:{b}')