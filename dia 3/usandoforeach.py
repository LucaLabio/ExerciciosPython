equipamentos = []
valor = []
nSerial = []
departamento =[]
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Digite o nome do equipamento: "))
    valor.append(float(input("Digite o valor do equipamento: ")))
    nSerial.append(int(input("Digite o Número Serial do equipamento: ")))
    departamento.append(input("Digite o Departamento: "))
    resposta=input("Digite \"S\" para continuar: ").upper()
for elemento in equipamentos:
    print("Equipamento: " + elemento)
for elemento in valor:
    print("O valor é R$" + elemento)
for elemento in nSerial:
    print("O número serial é " + elemento)
for elemento in departamento:
    print("O departamento é " + elemento)