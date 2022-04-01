'''Aprimore o desafio anterior, mostrando no final: A)A soma de todos os valores pares digitados; B)A soma dos valores da terceira coluna;
C) O maior valor da segunda linha'''

matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
soma_par = 0
soma_impar = 0
soma_valores = 0
maior = 0

for c in range(0, 3):
    for i in range(0, 3):
        matriz[c][i] = int(input(f"Digite o valor [{c}] [{i}]:"))
        if matriz[c][i] % 2 == 0:
            soma_par += matriz[c][i]
        if matriz[c][i] % 2 == 1:
            soma_impar += matriz[c][i]
        soma_valores += matriz[2][i]        #Se mudar o valor "2" para "1" o código não funciona. Mas se eu criar uma estrutura "for" a parte, funciona.
        if maior == 0:
            maior = matriz[1][i]
        if matriz[1][i] > maior:
            maior = matriz[1][i]

for c in range(0, 3):
    for i in range(0, 3):
        print(f"[{matriz[c][i]:^3}]", end="")
    print()
print(f"Pares total:{soma_par}\nÍmpares total:{soma_impar}\nA soma dos valores da terceira coluna é de: {soma_valores}\nO maior valor da linha 2 é:{maior}")