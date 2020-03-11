"""Neste mês, João recebeu um aumento no salário, porém ele não sabe calcular o percentual
de aumento. Você deverá escrever um algoritmo que recebe 2 números reais representando
os salários antes e depois do aumento e deverá calcular e exibir o percentual de aumento que
João obteve."""
antigo = float(input("Digite seu antigo salario"))
novo = float(input("Digite seu novo salario"))
porcentagem = (novo / antigo) *100
print("Houve um aumento de " + str(porcentagem) + "%")