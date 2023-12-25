#Estrutura condicional aninhada

nome = str(input('Digite seu nome:'))
if nome == 'Erik':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular!')
elif nome in 'Ana Cláudia Jéssia Juliana':
    print('Você têm um belo nome!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))
