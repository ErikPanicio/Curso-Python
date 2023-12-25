print('\033[30;45mOlá Mundo!') #A linha magenta vai até o final porque não foi dito a onde "fecha" a formatação
print('\033[30;45mOlá Mundo!\033[m') # <-- Modelo Correto

print('\033[33;44mOlá Mundo!\033[m') #(33)Texto amarelo;(44)Fundo azul
print('\033[7;33;44mOlá Mundo!\033[m') #(7)Inverte as cores:(33) Texto amarelo; (44) Fundo azul;Ficando fundo amarelo e texto azul

print('\033[30mOlá Mundo\033[m') #(30)Texto branco
print('\033[7;30mOlá Mundo\033[m') #(7)Inverte o (33)Texto branco para:Fundo branco
