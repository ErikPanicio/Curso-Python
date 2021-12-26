'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais
são as suas vogais'''

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador',
           'futuro')

for palavra in palavras:            #Vai pegar a palavra dentro de palavras; Ex: O valor de palavra é 0, então pegará a palavra aprender dentro da tupla palavras, esse valor 0 irá virar 1 e depois 2, por ser um for
    print(f'\nA palavra {palavra.upper()} tem às vogais:', end='')
    for letra in palavra:           #Vai pegar as letras na palavra; Ex: O valor de letra é 0 e o valor de palavra é 0, ele irá pegar a palavra 0 (aprender) e a letra 0 (a), e fará isso sucessivamente, porque é um for, o valor vai se alterar a cada repetição
        if letra in 'aeiou':
            print(letra, end='')


'''Palavra valerá 0, a palavra 0 é (Aprender); A letra 0 é (a), já que é um FOR o valor mudará a cada repetição, então, a letra 0 será (a),
ele irá ver se há a letra (a) in 'aeiou', se sim ele escreverá, na próxima repetição o valor de palavra será 1, que é a letra (p), ele irá ver se há
(p) in 'aeiou', se não, não escreverá. Isso vai ocorrer sucessivamente até acabar às letras, e então quando acabar às letras o FOR palavra
 se tornará 1, mudando assim sua palavra de (Aprender para Programar) e comparando assim às letras da palavra (Programar)'''