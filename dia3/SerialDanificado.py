""" um equipamento com um determinado número serial foi danificado e será descartado. Precisamos eliminar esse equipamento. """
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()
remocao = input("\nDigite o número serial do equipamento que sera descartado")
for i in range(0,len(seriais)):
    if remocao == seriais[i]:
        print("O equipamento descartado sera " + equipamentos[i])
        del equipamentos[i]
        del valores[i]
        del seriais[i]
        del departamentos[i]
        break

