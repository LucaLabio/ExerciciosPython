"""usuarios={}
opcao = input("O que deseja realizar? <I> para inserir | <P> para pesquisar | <E> para excluir | <L> para listar" ).upper()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        """ """chave=input("Digite o Login: ").upper()
        nome=input("Digite o nome: ").upper()
        data=input("Digite a ultima data de acesso: ")
        estacao=input("Qual a ultima estacao acessada: ").upper()
        usuarios[chave]=[nome,data,estacao]""" """
        chave = input("Digite o login: ").upper()
        usuarios[chave]=[input("Digite o nome: ").upper(),
                         input("Digite a ultima data de acesso: ").upper(),
                         input("Digite a ultima estacao acessada: " ).upper()]
    opcao = input("O que deseja realizar? <I> para inserir | <P> para pesquisar | <E> para excluir | <L> para listar" ).upper()"""

from dia6.dicionario_dados.funcoes import *
usuario={}
opcao=perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuario)
    if opcao=="P":
        pesquisar(usuario,input("Qual login deseja pesquisar? "))
    if opcao == "E":
        excluir(usuario,input("Qual login deseja excluir? "))
    if opcao == "L":
        listar(usuario)
    opcao = perguntar()