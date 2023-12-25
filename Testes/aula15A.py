total = 0

while True:     #Ira repetir infinitamente
    num = int(input('Digite um número (999 para parar):'))
    if num == 999:
        break
    total = total + num
print('O número digitado foi {}'.format(total))
