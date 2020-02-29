""" O usuário informa o valor de um boleto, o
percentual de juros cobrado e o numero de dias em atraso. O programa
calcula o novo valor a ser pago através da fórmula:
NOVO VALOR = VALOR BOLETO + (VALOR BOLETO * (JUROS/100)) * DIAS"""
boleto = float(input("informe o valor do boleto"))
juros = float(input("informe o percentual de juros cobrado por dia"))
dias = int(input("informe a quantidade de dias em atraso"))
valor = round(boleto+(boleto * (juros/100)) * dias)
print("o novo valor a ser pago é R$", valor)