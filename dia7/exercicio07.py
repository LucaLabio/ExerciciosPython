""" Faça um programa em Python que solicite ao usuário um número inteiro e
retorne se é múltiplo de 5 e de 10 ao mesmo tempo."""
n1 = int(input("Digite um numero "))
if n1 % 5 ==0 and n1 % 10 == 0:
    print("o numero digitado e multiplo de 5 e 10 ao mesmo tempo")
else:
    print("o numero digitado nao e multiplo de 5 e 10 ao mesmo tempo")