""" Escreva um algoritmo que calcula a área e o perímetro do círculo, use 3.141592 como valor de π. """
raio = float(input("Digite o valor do raio"))
pi = 3.141592
area = pi*(raio*raio)
perimetro = 2 * pi * raio
print("O perímetro do círculo é: " + str(perimetro))
print("A area do círculo é: " + str(area))