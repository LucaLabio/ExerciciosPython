"""Uma companhia aérea define os preços de suas
passagens a partir da informação do destino bem como
do número de passagens (se é apenas ida ou se inclui
também a volta). Faça um programa em Python que
solicite o destino bem como se o cliente deseja
somente ida ou ida e volta. Informe o preço de acordo
com a tabela abaixo (PS: a empresa não trabalha nos
trechos sul e sudeste). """
print("REGIÃO         IDA    IDA E VOLTA")
print("NORTE         R$280   R$400")
print("NORDESTE      R$380   R$628")
print("CENTRO-OESTE  R$620   R$1100")
viagem = input("Digite para qual regiao você gostaria de ir").upper()
ida = input("Informe se você quer apenas uma passagem de IDA ou IDA E VOLTA").upper()
while ida != "IDA" and ida != "IDA E VOLTA":
    ida = input("Informe se você quer apenas uma passagem de IDA ou IDA E VOLTA").upper()
while viagem != "NORTE" and viagem != "NORDESTE" and viagem != "CENTRO-OESTE":
    viagem = input("Digite para qual regiao você gostaria de ir").upper()
if viagem == "NORTE":
    if ida == "IDA":
        preco = 280
    else:
        preco = 400
elif viagem == "NORDESTE":
    if ida == "IDA":
        preco = 380
    else:
        preco = 628
else:
    if ida == "IDA":
        preco = 620
    else:
        preco = 1100
print("O preço da viagem sera R$" + str(preco))