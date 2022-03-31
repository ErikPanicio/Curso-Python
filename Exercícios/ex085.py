'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma única lista que mantenha separado os valores
pares e ímpares. No final mostre os valores pares e ímpares em ordem crescente'''

lista = [[], []]
for c in range(1, 8):
    valor = (int(input("Digite um número:")))
    if valor % 2 == 0:
        lista[0].append(valor)
    if valor % 2 == 1:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f"Os números pares são:{lista[0]}\nOs números ímpares são: {lista[1]}")
