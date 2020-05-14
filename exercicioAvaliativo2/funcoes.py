# Funcao para Vender passagem
def VenderPassagem(janela, corredor):
    pergunta = int(input("Digite o numero da opcao desejada \n"
                         "1- Cadeira na Janela \n"
                         "2- Cadeira no Corredor \n"))
    while pergunta != 1 and pergunta != 2:
        pergunta = int(input(" Essa nao eh uma opcao valida, digite o numero da opcao desejada \n"
                             "1- Cadeira na Janela \n"
                             "2- Cadeira no Corredor \n"))

    poltrona = int(input("Digite o numero da poltrona desejada, sao 24 acentos no total")) - 1
    while poltrona >= 24:
        poltrona = int(input("Essa nao eh uma opcao valida, Digite o numero da poltrona desejada")) - 1

    if pergunta == 1:
        if janela[poltrona] == 0:
            janela[poltrona] = 1
            print("Venda realizada com sucesso!")

        else:
            print("Poltrona ocupada. Venda não realizada!")
    else:
        if corredor[poltrona] == 0:
            corredor[poltrona] = 1
            print("Venda realizada com sucesso!")
        else:
            print("Poltrona ocupada. Venda não realizada!")


# Funcao Cancelar Passagem

def CancelarPassagem(janela, corredor):
    pergunta = int(input("Digite o numero da opcao desejada \n"
                         "1- Cadeira na Janela \n"
                         "2- Cadeira no Corredor \n"))
    while pergunta != 1 and pergunta != 2:
        pergunta = int(input(" Essa nao eh uma opcao valida, digite o numero da opcao desejada \n"
                             "1- Cadeira na Janela \n"
                             "2- Cadeira no Corredor \n"))

    poltrona = int(input("Digite o numero da poltrona desejada, sao 24 acentos no total")) - 1
    while poltrona >= 24:
        poltrona = int(input("Essa nao eh uma opcao valida, Digite o numero da poltrona desejada")) - 1

    if pergunta == 1:
        if janela[poltrona] == 1:
            janela[poltrona] = 0
            print("Compra cancelada com sucesso!")
        else:
            print("Poltrona livre. Compra não cancelada! ")
    else:
        if corredor[poltrona] == 1:
            corredor[poltrona] = 0
            print("Compra cancelada com sucesso!")
        else:
            print("Poltrona livre. Compra não cancelada! ")


# Funcao Mostrar mapa de ocupacao

def MostrarMapa(janela, corredor):
    for j in range(len(janela)):
        if janela[j] == 0:
            complemento_janela = "Livre"
        else:
            complemento_janela = "Ocupado"
        if corredor[j] == 0:
            complemento_corredor = "Livre"
        else:
            complemento_corredor = "Ocupado"
        print("Cadeira Janela ", j + 1, " - ", complemento_janela, "        Cadeira Corredor ", j + 1, " - ",
              complemento_corredor)
