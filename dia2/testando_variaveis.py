"""Testando diferentes variaveis"""
nome=input("Digite seu nome")
empresa=input("Digite o nome da sua empresa")
qtde_func=int(input("Digite a quantidade de funcionarios que trabalham na sua empresa"))
mediaSalar=float(input("Digite a media salarial da sua empresa"))
print(nome + " trabalha na empresa " + empresa)
print("Possui um total de ", qtde_func, " funcionarios")
print("A media de salario mensal é R$" + str(mediaSalar))
"""Testando o Type """
print("==============================VERIFICANDO TIPO DE DADO====================")
print("O tipo de variavel [nome] é ", type(nome))
print("O tipo de variavel [empresa] é ", type(empresa))
print("O tipo de variavel [qtde_func] é ", type(qtde_func))
print("O tipo de variavel [mediaSalar] é ", type(mediaSalar))