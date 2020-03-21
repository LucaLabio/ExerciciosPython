""". Escreva um algoritmo em Python que recebe dois números inteiros e exibe: a soma desses
dois números, a multiplicação, a divisão inteira e o resto da divisão inteira.
"""
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
soma = n1 + n2
multi = n1 * n2
divi = n1/n2
resto = n1 % n2
print("A soma dos dois números é " + str(soma))
print("A multiplicação dos dois números é " + str(multi))
print("A divisão dos dois números é " + str(divi))
print("O resto da divisão dos dois números é " + str(resto))