from exercicioAvaliativo3.funcoes import *

produtos = {}
tentativa = 0
senha = False
menu = int(input("Digite o numero da opcao desejada \n"
                 "1-Cadastrar Produto \n"
                 "2-Alterar Produto \n"
                 "3-Excluir produto \n"
                 "4-Listar estoque de peças \n"
                 "5-Comprar produto \n"
                 "6-Vender produto \n"
                 "7-Sair \n"))
while menu != 7:
    if menu == 1:
        cadastrar(produtos)
        print(produtos)
    if menu == 2:
        while tentativa < 3 and senha == False:
            resultado = verificarsenha(senha, tentativa)
            tentativa = resultado[0]
            senha = resultado[1]
        if senha:
            alterar(produtos)
        else:
            print("SEU ACESSO FOI BLOQUEADO! PROCURE O ADMINISTRADOR")
            break
    if menu == 3:
        while tentativa < 3 and senha == False:
            resultado = verificarsenha(senha, tentativa)
            tentativa = resultado[0]
            senha = resultado[1]
        if senha:
            excluir(produtos)
        else:
            print("SEU ACESSO FOI BLOQUEADO! PROCURE O ADMINISTRADOR")
            break
    if menu == 4:
        listar(produtos)
    if menu == 5:
        comprar(produtos)
    if menu == 6:
        vender(produtos)
    menu = int(input("Digite o numero da opcao desejada \n"
                     "1-Cadastrar Produto \n"
                     "2-Alterar Produto \n"
                     "3-Excluir produto \n"
                     "4-Listar estoque de peças \n"
                     "5-Comprar produto \n"
                     "6-Vender produto \n"
                     "7-Sair \n"))
