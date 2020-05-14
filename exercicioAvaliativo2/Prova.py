from exercicioAvaliativo2.funcoes import *

janela = [0 for zero in range(24)]
corredor = [0 for zero in range(24)]
menu = int(input("Digite o numero da opcao desejada \n"
                 "1-Vender Passagem \n"
                 "2-Cancelar Compra \n"
                 "3-Mostrar Mapa de Ocupacao \n"
                 "4-Sair \n"))
while menu != 4:
    if menu == 1:
        controle = False
        for percorrer in range(len(janela)):
            if janela[percorrer] == 0:
                controle = True
                break
        if controle == True:
            VenderPassagem(janela, corredor)
        else:
            print(" Ônibus lotado. Opção inválida!")
    if menu == 2:
        controle = False
        for percorrer in range(len(janela)):
            if janela[percorrer] == 1:
                controle = True
                break
        if controle == True:
            CancelarPassagem(janela, corredor)
        else:
            print("Todas as poltronas estão livres. Opção inválida!")
    if menu == 3:
        MostrarMapa(janela, corredor)
    menu = int(input("Digite o numero da opcao desejada \n"
                     "1-Vender Passagem \n"
                     "2-Cancelar Compra \n"
                     "3-Mostrar Mapa de Ocupacao \n"
                     "4-Sair \n"))
