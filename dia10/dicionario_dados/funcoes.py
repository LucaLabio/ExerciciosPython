def perguntar():
    resposta = input("O que deseja realizar? <I> para inserir | <P> para pesquisar | <E> para excluir | <L> para listar" ).upper()
    return resposta

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                     input("Digite a ultima data de acesso: "),
                                                     input("Digite a ultima estacao acessada: ").upper()]
    salvar(dicionario)
def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print("Nome.............: " + lista[0])
        print("Ultimo acesso....: " + lista[1])
        print("Ultima estacao...: " + lista[2])
    else:
        print("teste")
def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Objeto Deletado")
def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)
def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))