""" Faça um algoritmo em Python para ler dois números inteiros (num1 e num2)
e informar se num1 é divisível por num2."""
n1 = float(input("Digite um numero "))
n2 = float(input("Digite outro numero "))
if n1 % n2 == 0:
    print(n1," e divisivel por ",n2)
else:
    print(n1, " nao e divisivel por ", n2)