"""As casas de São Paulo estão recebendo o carnê do IPTU com duas opções de pagamento:
à vista ou em 10 vezes. Sua tarefa é desenvolver um programa/algoritmo onde o usuário
informa (digita) o valor total à vista e o valor de cada parcela. Seu programa imprime o
desconto em percentual dado pela prefeitura para pagamento à vista."""
avista = float(input("Digite o valor à vista"))
parcela = float(input("Digite o valor de cada parcela")) * 10
desconto = int(100 - ((avista/parcela)*100))
print("o percentual de desconto para pagamento à vista é " + str(desconto) + "%")