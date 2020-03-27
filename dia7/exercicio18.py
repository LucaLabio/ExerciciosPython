""" Faça um programa em Python que mostre o menu de opções a seguir:
Menu de Opções
1. Somar dois números
2. Raiz quadrada de um número
Digite a opção desejada:
Receba a opção do usuário e os dados necessários para executar cada
operação."""
import math
menu = input("selecione uma das opcoes a seguir \n1.Somar dois numeros \n2.Raiz Quadrada de um numero")

if menu == "1":
    n1 = int(input("Digite um numero "))
    n2 = int(input("Digite outro numero "))
    print("Voce desejou mostrar o resultado da soma: ", n1+n2)
else:
    n1 = int(input("Digite um numero "))
    n1 = math.sqrt(n1)
    print("Voce desejou mostrar a raiz quadrada: ", n1)