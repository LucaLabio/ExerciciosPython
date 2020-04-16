"""Faça um programa em Python que receba o preço de um produto, a categoria (1 - limpeza, 2 - alimentação ou 3 - vestuário) e a situação (R - produtos que necessitam de refrigeração e N - produtos que não necessitam de refrigeração).  Calcule e mostre:* O valor do aumento, usando as regras que se seguem:
*O valor do imposto, usando as regras a seguir.*O produto que preencher pelo menos um dos seguintes requisitos pagará imposto equivalente a 5% do preço, caso contrário, pagará 8%. Os requisitos são:  Categoria:2  Situação: R*O novo preço, ou seja, o preço mais aumento menos imposto.*A classificação, usando as regras a seguir:
"""
preco = float(input("Digite o preco do produto"))
categoria = int(input("Digite o numero da categoria: 1- limpeza | 2- alimentacao | 3- vestuario"))
situacao = input("Digite a situacao do produto: 'R' - produtos que necessitam de refrigeração | 'N' - produtos que não necessitam de refrigeração").upper()
precoimposto = 0
aumento = 0
if preco <= 25:
    if categoria == 1:
        preco = preco * 1.05
        aumento = 5
    elif categoria == 2:
        preco = preco * 1.08
        aumento = 8
    else:
        preco = preco * 1.10
        aumento = 10
else:
    if categoria == 1:
        preco = preco * 1.12
        aumento = 12
    elif categoria == 2:
        preco = preco * 1.15
        aumento = 15
    else:
        preco = preco * 1.18
        aumento = 18
if categoria == 2 or situacao == "R":
    precoimposto = 1.05
else:
    precoimposto = 1.08
preco = preco / precoimposto
print("o percentual de aumento foi de ",aumento,"% e o percentual de imposto foi de ", str(precoimposto-1*100), " % e o preco final totalizou em ",preco)
if preco <= 50:
    print("O preco eh considerado barato")
elif preco == 50 or preco <= 120:
    print("o preco eh considerado normal")
else:
    print("o preco eh considerado caro")
