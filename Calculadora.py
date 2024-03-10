print('''Seja bem vindo!! :)''')
numero1 = int(input("digite um numero:"))
operacao = input('Digite a operação:')
numero2 = int(input("digite um numero:"))
resultado = ''
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '/':
    resultado = numero1 / numero2
elif operacao == '*':
    resultado = numero1 * numero2
else:
    resultado =':  ops.. desculpe :( Reinicie o programa. '

print(str(numero1) + ' ' + str(operacao) + ' ' + str(numero2) + ' = ' + str(resultado))

reiniciar = int(input("reiniciar a calculadora? 1- sim / 2- nao:"))
reiniciar= int(input(" "))
