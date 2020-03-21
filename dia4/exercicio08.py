"""Dados o preço de um produto e um percentual de desconto, escreva um algoritmo que calcula
e mostra o valor do desconto e o novo preço do produto dado o percentual. E se, ao invés
de um desconto, fosse um aumento. O que muda no seu algoritmo?"""
preco = float(input("Digite o preço do produto: "))
desconto = int(input("Digite a porcentagem de desconto: ")) / 100
aumento = int(input("Digite a porcentagem de incremento: ")) / 100
reducao = preco * (1 - desconto)
incremento = preco * (1 + aumento)
print("O Preço original era " + str(preco))
print("O preço com desconto ficou " + str(reducao))
print("O preço com aumento ficou " + str(incremento))
