# Verificacao estoque
def verificarestoque(estoque):
    while not estoque.isdigit() or int(estoque) <= 0:
        print("A quantidade de estoque deve ser maior que 0")
        estoque = input('Digite a quantidade em estoque')
    return int(estoque)

def verificarsenha(senha, tentativas):
    password = input('Digite a Senha de acesso')
    if password == 'yN1825*a':
        senha = True
    else:
        print('SENHA INCORRETA')
        tentativas = tentativas + 1
    return tentativas, senha

def verificarcodigo(codigo):
    while not codigo.isdigit() or int(codigo) < 0:
        print("O codigo deve ser maior ou igual a 0")
        codigo = input('Digite o Codigo do produto')
    return int(codigo)

# Funcao comprar
def cadastrar(produtos):
    codigo = verificarcodigo(input("Digite o Codigo do produto"))
    descricao = input("Digite a descricao do produto")
    estoque = verificarestoque(input("Digite a quantidade em estoque"))
    if codigo in produtos:
        print("Codigo ja cadastrado")
    else:
        produtos[codigo] = {'estoque': estoque, 'descricao': descricao}

# Funcao Alterar
def alterar(produtos):
    alterado = int(input('Digite o codigo do produto a ser alterado'))
    if alterado in produtos:
        print(produtos[alterado])
        menu = int(input('Voce deseja: \n'
                         '1-Alterar Descricao \n'
                         '2-Alterar Quantidade em estoque \n'
                         '3-Sair'))
        while menu != 3:
            if menu == 1:
                descricao = input('Digite a nova descricao do produto')
                produtos[alterado]['descricao'] = descricao
            elif menu == 2:
                estoque = verificarestoque(input('Digite a nova quantidade em estoque'))
                produtos[alterado]['estoque'] = estoque
            menu = int(input('Voce deseja: \n'
                             '1-Alterar Descricao \n'
                             '2-Alterar Quantidade em estoque \n'
                             '3-Sair'))
        print(produtos[alterado])
    else:
        print('PRODUTO NÃO CADASTRADO')

def excluir(produtos):
    excluido = int(input('Digite o codigo do produto a ser excluido'))
    if excluido in produtos:
        print(produtos[excluido])
        pergunta = input('DESEJA EXCLUIR O PRODUTO?').upper()
        if pergunta == 'SIM' or pergunta == 'S':
            del produtos[excluido]
            print('PRODUTO EXCLUIDO COM SUCESSO')
        else:
            print('PRODUTO NÃO EXCLUÍDO')
    else:
        print('PRODUTO NÃO CADASTRADO')


def listar(produto):
    def contar(produto, quantidade=0, excessoes=0, x=0):
        estoque = produto[list(produto.keys())[x]]['estoque']
        quantidade += estoque
        if estoque < 100:
            excessoes += 1
        if x < len(produto) - 1:
            return contar(produto, quantidade, excessoes, x + 1)
        else:
            return {'quantidade': quantidade, 'excessoes': excessoes}

    conta = contar(produto)
    codigos = list(produto.keys())
    codigos.sort()
    print('CODIGO \t DESCRICAO \t ESTOQUE \n'
          '—————— \t ————————— \t ———————')
    for codigo in codigos:
        print('{} \t {} \t {}'.format(codigo, produto[codigo]['descricao'], produto[codigo]['estoque']))
    print('Total de produtos cadastrados: ' + str(len(codigos)))
    print('Quantidade de itens em estoque: ' + str(conta['quantidade']))
    print('Produtos com estoque abaixo do mínimo permitido (100 unidades): ' + str(conta['excessoes']))

def comprar(produtos):
    checar = verificarcodigo(input('Digite o codigo do produto a ser comprado'))
    if checar in produtos:
        print(produtos[checar])
        compra = int(input('Digite a quantidade de produtos que deseja comprar'))
        while compra <= 0:
            compra = int(input('Digite a quantidade de produtos que deseja comprar, o valor deve ser maior que 0'))
        produtos[checar]['estoque'] += compra
    else:
        print('PRODUTO NÃO CADASTRADO')

def vender(produtos):
    checar = verificarcodigo(input('Digite o codigo do produto a ser comprado'))
    if checar in produtos:
        print(produtos[checar])
        venda = int(input('Digite a quantidade de produtos que deseja vender'))
        while venda <= 0:
            venda = int(input('Digite a quantidade de produtos que deseja vender, o valor deve ser maior que 0'))
        if venda > produtos[checar]['estoque']:
            print('A quantidade de produtos solicitados é maior que a presente no estoque, Venda negada')
        else:
            produtos[checar]['estoque'] -= venda
    else:
        print('PRODUTO NÃO CADASTRADO')