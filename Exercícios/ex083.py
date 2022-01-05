'''Crie um programa onde o usuário digite uma expressão (matemática) qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão
passada está com os parênteses abertos e fechados na ordem correta'''

expressao = str(input('Digite um expressão matemática:'))

if expressao.count('(') == expressao.count(')'):
    print('Os parênteses estão fechados corretamente')
else:
    print('Os parênteses \033[31mnão\033[m estão fechados corretamente')
print(expressao.count('('))
