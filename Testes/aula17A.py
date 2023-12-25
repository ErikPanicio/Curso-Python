num = [2, 5, 9, 1]
num[0] = 10     #Adiciona o valor 10 ao valor do índice 0
num.append(15)  #Adiciona mais um índice (elemento) no final
num.insert(0, 5)#Insere um valor na posição desejada e joga os outros valores para o lado
num.sort()      #Organiza de forma crescente
num.sort(reverse=True)  #Organiza de forma decrescente
num.pop()       #Remove o último valor e índice
num.remove(5)   #Remove o valor desejado, se haver dois valores iguais ele remove o primeiro
print(num)