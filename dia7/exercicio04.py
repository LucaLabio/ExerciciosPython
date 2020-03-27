"""Faça um programa em Python que receba do usuário três números inteiros e
mostre-os na tela em ordem crescente. Caso o usuário digite três números
iguais, mostrar na tela a informação: OS TRÊS NÚMEROS DIGITADOS SÃO
IGUAIS."""
n1 = [int(input("Digite um numero ")), int(input("Digite um segundo numero ")), int(input("Digite um terceiro numero "))]
if n1[0] == n1[1] and n1[0] == n1[2]:
    print("OS TRÊS NÚMEROS DIGITADOS SÃO IGUAIS")
else:
    n1.sort()
    print(n1)