'''Crie um tupla preenchida com os 20 primeiros colocados ta Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A)Apenas os 5 primeiros colocados; B)Os últimos 4 colocados da tabela; C)Uma lista com os times em ordem alfabética; D)Em que posição
na tabela está o time da Chapecoense'''

colocados = ('Atlético-MG', 'Flamengo', 'São Paulo', 'Internacional', 'Fluminense', 'Palmeiras', 'Santos', 'Grêmio', 'Athletico-PR',
             'Bahia', 'Fortaleza', 'Atlético-GO', 'Bragantino', 'Corinthians', 'Sport Recife', 'Ceará SC', 'Vasco da Gama',
             'Coritiba', 'Botafogo', 'Goiás')

print(f'Os 5 primeiros colocados foram: {colocados[0:5]}')
print(f'Os últimos 4 colocados foram: {colocados[-4:]}')
print(f'Os times em ordem alfabética são:{sorted(colocados)}')
print(f'O time do Santos aparece na posição:{colocados.index("Santos")+ 1}')

