"""Calcula o volume cúbico de uma lata de óleo.
O usuário informa a altura e o valor de r. O programa calcula através
da fórmula VOLUME = 3.14 * (R * R) * ALTURA. """
altura = float(input("informe o valor da altura da lata"))
r = float(input("Informe o valor do raio da lata"))
volume = round(3.14 * (r * r) * altura,2)
print("o volume total da lata é ", volume)