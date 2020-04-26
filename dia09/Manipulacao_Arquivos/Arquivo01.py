"""arquivo = open("arquivoteste.txt","w")
arquivo.write("Teste")
arquivo.close()"""

"""with open("arquivoteste.txt","w") as arquivo:
    arquivo.write("\nTeste2")"""

"""with open("arquivoteste.txt","r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)"""
with open("arquivoteste.txt","r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)