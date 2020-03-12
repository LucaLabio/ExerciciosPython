""" Faça o teste de mesa para numero_1= 15 e numero_2= 6
resultado = ((numero_1%2)*3)+(13-2+numero_2)
Responda:
a) Qual o conteúdo da variável resultado quando termina o
algoritmo?
b) Analise o pseudocódigo e responda: o que mostrará na tela?
c) Reescrever o algoritmo utilizando a linguagem de programação
Python. """
n1 = int(input("Digite um numero inteiro"))
n2 = int(input("Digite um numero inteiro"))
resultado = ((n1%2)*3)+(13-2+n2)
if resultado <= 0:
    print("Resultado é menor ou igual a zero")
elif resultado>0 and resultado<=20:
    print("Resultado é maior que zero e menor ou igual a 20")
else:
    print("Resultado maior que 20")