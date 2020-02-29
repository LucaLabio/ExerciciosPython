""" Deve ser informado o preço do litro do
combustível e o valor em dinheiro que se deseja abastecer. O programa
mostra quantos litros serão comprados. (Ex. a gasolina custa R$ 4,30 e
o motorista quer abastecer R$ 50,00)."""
print("o preco do combustivel é R$4.50")
gasolina = 4.50
comprar = float(input("Digite quanto você quer usar de dinheiro para pagar"))
resultado = round(comprar/gasolina,2)
print("Você conseguira comprar um total de ", resultado, "litros")