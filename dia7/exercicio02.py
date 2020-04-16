""" Faça um programa em Python que receba dois números inteiros e mostre na
tela o maior número digitado."""
n1 = int(input("Digite um numero "))
n2 = int(input("Digite outro numero"))
if n1 > n2:
    print("O maior numero é ", n1)
elif n1 == n2:
    print("os numeros tem o mesmo valor")
else:
    print("O maior numero é ", n2)