inventario = []
resposta = "S"
while resposta == "S":
    equipamento = [input("Digite o nome do equipamento"),
            float(input("Digite o valor")),
            int(input("Digite o numero serial")),
            input("Digite o nome do departamento")]
    inventario.append(equipamento)
    resposta = input("Digite \"S\" para continuar").upper()

for elemento in inventario:
    print("nome.......:", elemento[0])
    print("valor.......:", elemento[1])
    print("serial.......:", elemento[2])
    print("departamento.......:", elemento[3])
#busca de valores
busca = input("\nDigite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
    if busca == elemento[0]:
        print("Valor...", elemento[1])
        print("Serial...", elemento[2])
#depreciação de valor
depreciacao = input("\nDigite o nome do equipamento que sera depreciado: ")
for elemento in inventario:
    if depreciacao == elemento[0]:
        print("Valor antigo R$", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Novo valor R$", elemento[1])
#exclusao de serial
serial = int(input("\nDigite o serial a ser excluido"))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove((elemento))
for elemento in inventario:
    print("nome.......:", elemento[0])
    print("valor.......:", elemento[1])
    print("serial.......:", elemento[2])
    print("departamento.......:", elemento[3])

"""funções para listas numericas"""
valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores)>0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))