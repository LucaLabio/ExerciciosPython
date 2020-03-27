""" Escreva um programa em Python que receba 3 números reais e mostre-os na
tela em ordem decrescente. Considere que o usuário digitará 3 números
diferentes."""
n1 = [int(input("Digite um numero ")), int(input("Digite um segundo numero ")), int(input("Digite um terceiro numero "))]
n1.sort()
n1 = n1[::-1]

print(n1)