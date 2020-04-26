"""Faça um programa em Python que solicite ao usuário um número inteiro e mostre na tela os próximos 10 números inteiros a partir do número digitado."""
numero = int(input("Digite um numero inteiro"))
print("o numero inteiro eh" , numero)
for i in range(1,11,1):
    print("o proximo numero inteiro eh: ", numero + i)