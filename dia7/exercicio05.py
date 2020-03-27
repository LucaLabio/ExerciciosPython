""" Escreva um programa em Python que solicite ao usuário 3 (três) números
inteiros e retorne se os números foram ou não foram digitados em ordem
crescente.
Exemplo 1:
Digite 3 (três) números inteiros:
45
65
44
Os números não foram digitados em ordem crescente."""
n1 = [int(input("Digite um numero ")), int(input("Digite um segundo numero ")), int(input("Digite um terceiro numero "))]
n2 = []
help = 0
for i in range(0,len(n1),1):
    n2.append(n1[i])
n2.sort()
for i in range(0,len(n1),1):
    if n1[i] == n2[i]:
        help = help + 1
if help == 3:
    print("Os números foram digitados em ordem crescente")
else:
    print("Os números não foram digitados em ordem crescente")