"""Elabore um programa em Python que seja capaz de contar a quantidade de números ímpares existentes entre dois números fornecidos pelo usuário."""
n1 = int(input("Digite um numero"))
n2 = int(input("Digite outro numero"))
for i in range(n1,n2,1):
    if i % 2 != 0:
        print("o numero ",i," eh impar")