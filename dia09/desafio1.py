"""Faça um programa em Python que gere números inteiros aleatórios entre 100 e  110.  Calcular  a  soma  dos  números  gerados  até  que  o  número  n1  (valor informado pelo usuário) seja gerado.Função: randint(inicio,fim) do módulo radom"""
from random import *
n1 = int(input("digite um numero maior que 200"))
total = 0
while n1 < 200:
    n1 = int(input("digite um numero maior que 200"))
while total < n1:
    total += randint(100,110)
    print(total)
    if total > n1:
        total = 0
print(n1)