""" Faça um programa em Python que receba dois números inteiros e mostre na
tela o maior número digitado."""
n1 = float(input("Digite um numero "))
n2 = float(input("Digite outro numero"))
if n1 > n2:
    print("O primeiro numero e maior")
elif n1 == n2:
    print("os numeros tem o mesmo valor")
else:
    print("O segundo numero e menor")