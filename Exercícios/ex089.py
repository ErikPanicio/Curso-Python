'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostrem um boletim contendo
a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente'''

lista = []
lista_organizada = []
continuar = "S"
numero = 0

while continuar == "S":
    nome = lista.append(str(input("Digite o nome:")))
    nota1 = lista.append(float(input("Digite a primeira nota:")))
    nota2 = lista.append(float(input("Digite a segunda nota:")))
    lista_organizada.append(lista[:])
    lista.clear()
    continuar = str(input("Deseja continuar?[S/N]:")).upper()
print("-" * 25)
for c in range(0, len(lista_organizada)):
    print(f"Nº{c} Nome:{lista_organizada[c][0]} Média:{(lista_organizada[c][1] + lista_organizada[c][2])/2}")
print("-" * 25)
while True:
    numero = int(input("Deseja mostrar a nota de qual aluno? [999 interrompe]:"))
    if numero == 999:
        break
    else:
        print(f"Nome:{lista_organizada[numero][0]}\nNota1:{lista_organizada[numero][1]}\nNota2:{lista_organizada[numero][2]}")

