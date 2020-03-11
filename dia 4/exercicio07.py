"""Uma pessoa tem em seu guarda roupa x camisas, y calças e z pares de sapato. Escreva
um algoritmo que calcula de quantas maneiras diferentes ele pode se vestir. Seu algoritmo
deverá ler o número de camisas, o número de calças e o número de pares de sapato."""
camisa = int(input("Digite quantas camisas você tem: "))
calsa = int(input("Digite quantas calsas você tem: "))
par = int(input("Digite quantos pares de sapato você tem: "))
total = camisa * calsa * par
print("Você tem um total de " + str(total) + " maneiras diferentes de se vestir")