"""Um comerciante comprou um produto e quer vendê-lo com um lucro de 45%
se o valor da compra for menor que R$ 20,00; caso contrário, o lucro será de
30%. Elabore um algoritmo em Python que leia o valor do produto e mostre na
tela o valor de venda para o produto."""
valor = float(input("Digite o valor de compra"))
preco = 0
if valor < 20:
    preco = (valor * 145) / 100
else:
    preco = (valor * 130)/ 100
print("O preco de venda sera: R$",preco)