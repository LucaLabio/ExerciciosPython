"""Faça um algoritmo em Python para ler três valores reais e informar se estes
podem ou não formar os lados de um triângulo e qual tipo de triângulo seria:
equilátero, isósceles ou escaleno.
"""
lado1 = float(input("Digite o valor de um lado "))
lado2 = float(input("Digite o valor de outro lado"))
lado3 = float(input("Digite o valor de outro lado"))
if lado1 == lado2 and lado1 ==lado3:
    print("Triangulo equilatero ")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("Triangulo Escaleno")
else:
    print("Triangulo isosceles")