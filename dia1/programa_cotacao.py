"""O usuário digita quanto está valendo o dólar
e quanto em reais ele possui. O programa exibe quantos dólares vale os
reais que o usuário informou. """
dolar = float(input("Digite o valor atual do dolar"))
reais = float(input("Digite quanto você possui em reais"))
conversao = round(reais/dolar,2)
print("Convertendo seu dinheiro para dolares você totaliza $", conversao, " dolares")
