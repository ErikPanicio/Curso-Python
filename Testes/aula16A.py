#Tuplas são imutáveis

lanche = ('Hambúger', 'Suco', 'Pizza', 'Pudim')

print(lanche[0])

for c in lanche:
    print(f'{c}')

a = (1 , 2, 3)
b = (4, 5, 6)
c = a + b
print(c)
c = b + a
print(c)