""" Elabore um algoritmo em Python que indique se um número digitado está
compreendido entre 0 e 30 ou entre 40 e 79 ou fora dos limites estabelecidos."""
n1 = int(input("Digite um numero"))
if n1 >= 0 and n1 <= 30 or n1 >= 40 and n1 <= 79:
    print("Voce digitou um numero dentro dos valores compreendidos")
else:
    print("Voce digitou um numero fora dos limites estabelecidos")
